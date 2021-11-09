import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    

    def __init__(self,):  
        """Bloque raiz"""
        gr.sync_block.__init__(
            self,
            name='raiz_cuadrada',   
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        
    def work(self, input_items, output_items):
        x=input_items[0]
        y=output_items[0]
        y[:]=np.sqrt(x)
        return len(x)
        

