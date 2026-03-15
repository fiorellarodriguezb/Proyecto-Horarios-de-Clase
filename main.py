
from sistema import sistema

def main(api_t1,api_t2,api_t3,api_profesores):
    sistema = sistema()
    # menu de arranque  
    sistema.menu_arranque(api_t1,api_t2,api_t3,api_profesores)
    
    
api_t1 = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-1.json"
api_t2 = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2526-2.json"
api_t3 = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/materias2425-3.json"
api_profesores = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-2/refs/heads/main/profesores.json"
main(api_t1,api_t2,api_t3,api_profesores)