import hashlib
import hashlib

def calculateHash256():
    # entrada=str(self.previous_block_hash)
    # entrada=entrada+str(self.transaction.public_key.publicExponent)
    # entrada=entrada+str(self.transaction.public_key.modulus)
    # entrada=entrada+str(self.transaction.message)
    # entrada=entrada+str(self.transaction.signature)
    # entrada=entrada+str(self.seed)
    previous_block_hash = 412828392020675584641083509410291074805340152571696570113062152990180712646
    publicEx = 65537
    mod = 14874116360765734651997711401943638509292751535771224423995634971116949685234149496460823779757547833132097239753221487027136807533808810944050013886394505962654226728062781350706018450260941392471197282058256030593707854714490109680386711070220507454966121556236440377175549493604596843442996539972145654567468024903024158940964686502675063145599208118503922098820342057890562219349584099874658079224801678773071661879104732167487136482121740826852112395318613744734202799100001595999678152843563886237274840607450113736918509339503220706219711950188477480290746594914136369598148130718143933518651433962644121152279
    message = 70654749831812497554948481828525141145026183319777113718072565226100966357740
    signature = 12031319185072073429185013330133936135781753016569677917014728026548852242071422265869452074553907125348412252550489509276172396930964504827596373249793892768358565110242596987759723510411399649194492078448514216181559754635107307534446421040419650702968844300976451881936605118477219159320464218452078354955169408908090062529705788635929099797357197819514391476460207606150659522216524496226761507201966714660486590569214912277628175860918422539176244986110352197657071288156918634596387365263206472325072445959689629356787543275641200963801656017504671100254270680051329569552064520206736240939104885820871506042917
    seed = 3141616893484978304049201744768712479275452045190884407278968924693792067814603449

    entrada=str(previous_block_hash)
    entrada=entrada+str(publicEx)
    entrada=entrada+str(mod)
    entrada=entrada+str(message)
    entrada=entrada+str(signature)
    entrada=entrada+str(seed)

    h=int(hashlib.sha256(entrada.encode()).hexdigest(),16)
    print(previous_block_hash)
    print()
    print(publicEx)
    print()
    print(mod)
    print()
    print(message)
    print()
    print(signature)
    print()
    print(seed)
    print()
    print(h)
    print()
    print()
    print()
    return h

def signature():
    message = 70654749831812497554948481828525141145026183319777113718072565226100966357740
    signature = 12031319185072073429185013330133936135781753016569677917014728026548852242071422265869452074553907125348412252550489509276172396930964504827596373249793892768358565110242596987759723510411399649194492078448514216181559754635107307534446421040419650702968844300976451881936605118477219159320464218452078354955169408908090062529705788635929099797357197819514391476460207606150659522216524496226761507201966714660486590569214912277628175860918422539176244986110352197657071288156918634596387365263206472325072445959689629356787543275641200963801656017504671100254270680051329569552064520206736240939104885820871506042917
    mod = 14874116360765734651997711401943638509292751535771224423995634971116949685234149496460823779757547833132097239753221487027136807533808810944050013886394505962654226728062781350706018450260941392471197282058256030593707854714490109680386711070220507454966121556236440377175549493604596843442996539972145654567468024903024158940964686502675063145599208118503922098820342057890562219349584099874658079224801678773071661879104732167487136482121740826852112395318613744734202799100001595999678152843563886237274840607450113736918509339503220706219711950188477480290746594914136369598148130718143933518651433962644121152279
    publicEx = 65537

    verifyMessage = pow(signature, publicEx, mod)
    print (verifyMessage)
    print (message)



calculateHash256()
signature();
