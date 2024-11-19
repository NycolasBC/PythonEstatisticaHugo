import pandas as pd

df = pd.read_excel('IdadeAltura.xlsx', sheet_name='IdadeAltura')
df_numerico = df.select_dtypes(include='number')

if not df_numerico.empty:
    df_media = df_numerico.mean()
    df_mediana = df_numerico.median()
    df_modo = df_numerico.mode()
    df_std = df_numerico.std()
    df_skew = df_numerico.skew()
    
    print("Valores médios da distribuição:")
    print(df_media, "\n")
    
    print("Valores medianos da distribuição:")
    print(df_mediana, "\n")
    
    print("Exibindo modo da distribuição:")
    print(df_modo.iloc[0], "\n")
    
    print("Exibindo desvio padrão da distribuição:")
    print(df_std, "\n")
    
    print("Exibindo assimetria da distribuição:")
    print(df_skew, "\n")
else:
    print("Nenhuma coluna numérica encontrada no conjunto de dados.")