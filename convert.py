# These functions need to be implemented
class CidrMaskConvert:

    INVALID_MESSAGE = 'Invalid'

    def cidr_to_mask(self, val):
        cidr = int(val)
        if cidr < 1 or cidr > 32:
            return self.INVALID_MESSAGE
        mask = ''
        for t in range(4):
            if cidr > 7:
                mask += '255.'
            else:
                if cidr > 0:
                    n = 0
                    for i in range(cidr,0,-1):
                        n += 2**(8-i)
                    mask += str(n) + '.'
                else: mask += str(cidr) + '.'
            cidr -= 8
            if cidr < 0:
                cidr = 0
    
        return mask[:-1]

    def mask_to_cidr(self, val):
        mask = val.split('.')
        if  not IpValidate.validate_size(mask):
            return self.INVALID_MESSAGE
        else:
            if mask[0] == "0":
                return self.INVALID_MESSAGE
            elif '' in mask:
                return self.INVALID_MESSAGE
            else:
                cidr = 0
                for octet in mask:
                    if not IpValidate.validate_octet(octet):
                        return self.INVALID_MESSAGE
                    else:
                        if not self.validate_octet(octet):
                           return self.INVALID_MESSAGE
                        else:
                            binary = bin(int(octet))[2:]
                            for character in binary:
                                cidr += int(character)
                return str(cidr)


    @staticmethod
    def validate_octet(val):
        n=255
        if int(val) == n:
            return True
        else:
            for i in range(0,8):
                n-=2**i
                if int(val) == n:
                    return True
            return False
            

class IpValidate:

    def ipv4_validation(self, val):
        address=val.split('.')
        if not IpValidate.validate_size(address):
            return False
        else:
            for octet in address:
                if not self.validate_octet(octet):
                    return False
            return True
        
    @staticmethod
    def validate_size(val):
        if len(val) !=4:
            return False
        else: return True

    @staticmethod
    def validate_octet(val):
        try:
            if (val == '0'):
                return True
            elif (int(val)):
                if (int(val) < 0 or int(val) > 255):
                    return False
                else: return True
        except ValueError:
            return False
