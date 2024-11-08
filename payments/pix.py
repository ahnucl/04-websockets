# import uuid
from uuid import uuid4
import qrcode


class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        # criar o pagamento na isntituição financeira
        # bank_payment_id = uuid.uuid4()
        bank_payment_id = uuid4()
        
        # codigo_copia_e_cola_123
        hash_payment = f'hash_payment_{bank_payment_id}'
        
        # qr code
        img = qrcode.make(hash_payment)
        
        # salvar imagem como arquivo png
        img.save(f"static/img/qr_code_payment_{bank_payment_id}.png")
        
        return {"bank_payment_id": bank_payment_id, 
                "qr_code_path": f"qr_code_payment_{bank_payment_id}",}