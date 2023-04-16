# /* ****************************************************************** **
# **    OpeSRANE - Open Software for Risk Assessment of Natech Events   **
# **                                                                    **
# **                                                                    **
# **                                                                    **
# ** (C) Copyright 2022, Bijan Sayyafzadeh                              **
# **                                                                    **
# ** All Rights Reserved.                                               **
# **                                                                    **
# ** Commercial use of this program without express permission of the   **
# ** owner (Bijan SayyafZadeh and following Developers), is             **
# ** strictly prohibited.  See file 'COPYRIGHT'  in main directory      **
# ** for information on usage and redistribution,  and for a            **
# ** DISCLAIMER OF ALL WARRANTIES.                                      **
# **                                                                    **
# ** Developed by:                                                      **
# **   Bijan SayyafZadeh (B.Sayyaf@yahoo.com)                           **
# **   MehDi Sharifi                                                    **
# **   Abdolreza Sarvghad Moghaddam                                     **
# **   ----- -----                                                      **
# **                                                                    **
# ** ****************************************************************** */

#This is a Sample File and any new Model is better to be constructed by a copy of this file
from opensrane.Misc._NewClass import _NewClass
from .ObjManager import *
from ._GlobalParameters import _GlobalParameters
import math as _math
import opensrane as _opr

class SimultaniousLiquid(_NewClass,_GlobalParameters):
    
    '''
    OutFlow Model For Liquid Complete OutFlow Simulaneously
    Release_Ratio: Ratio of the substance that release simultanously. (The Following Calculations will be done on the released volume and the remain substance will be eliminated by the code)
    
    
    '''
    Title='SimultaniousLiquid'
    
    def __init__(self,tag,Release_Ratio=1):
        
        #---- Fix Part for each class __init__ ----
        ObjManager.Add(tag,self)
        _NewClass.__init__(self,tag)
        #------------------------------------------
        
        
        _GlobalParameters.__init__(self)
        
        self.Release_Ratio=Release_Ratio
        
        
        self.name=f'SimultaniousLiquid '

        self.wipeAnalysis()
    
    def wipeAnalysis(self):
        # properties that are defined in _GlobalParameters should also be reset
        self.wipeAnalysisGlobal()
        
        # properties that are not constant and among each analysis will change should be define here
        pass

        
    def Calculate(self):
        
        Release_Ratio=self.Release_Ratio
        
        UnitObject=self.UnitObject #self.UnitObject has been defined in _GlobalParameters
        if UnitObject==None:         
            raise 'Error: self.UnitObject is emptey and before any usage it should be assigned before'
        

        
        SubstanceObject=_opr.Substance.ObjManager[UnitObject.SubstanceTag]
        SiteObject=_opr.Sites.ObjManager.Objlst[0]
         
        
        Pout=SiteObject.Pressure        #OutSide Pressure
        Tout=SiteObject.Temperature      #OutSide Temperature
        
        Pin=UnitObject.Pressure         #Inside Pressure
        Tin=UnitObject.Temperature       #Inside Temperature
        
        d=UnitObject.d_Storage          #Tank Diameter

 
        Vsubs=UnitObject.V_subs

     
        Rho=SubstanceObject.Density
        M=Vsubs*Rho*Release_Ratio                    #Initial Mass of the Substance
        
        

        t_release=[0,0.01]
        MassLiquidReleaseRate=[0, M/0.01]
        dMass_release=[0, M]
        TotalMass_Release=[0, M]
    
        self.t_release=t_release
        self.MassLiquidReleaseRate=MassLiquidReleaseRate
        self.dMassLiquid_release=dMass_release   
        self.TotalMassLiquid_Release=TotalMass_Release 
            
        self.MassGasReleaseRate=[0 for i in self.t_release]
        self.dMassGas_release=[0 for i in self.t_release]
        self.TotalMassGas_Release=[0 for i in self.t_release]               
            

       
        return 0
        
        