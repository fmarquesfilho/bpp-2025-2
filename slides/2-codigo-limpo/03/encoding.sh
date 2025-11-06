#!/bin/bash

# Script para converter todos os arquivos na pasta examples
cd examples/

for file in *; do
    if [ -f "$file" ]; then
        echo "Processando: $file"
        
        # Tenta detectar encoding
        encoding=$(file -I "$file" | awk -F'charset=' '{print $2}')
        
        # Remove caracteres inválidos e converte para UTF-8
        iconv -f ISO-8859-1 -t UTF-8//TRANSLIT "$file" > "${file}.temp"
        
        # Verifica se a conversão foi bem-sucedida
        if [ $? -eq 0 ]; then
            mv "${file}.temp" "$file"
            echo "✅ Convertido: $file para UTF-8"
        else
            # Tenta com outro encoding comum
            iconv -f WINDOWS-1252 -t UTF-8//TRANSLIT "$file" > "${file}.temp"
            if [ $? -eq 0 ]; then
                mv "${file}.temp" "$file"
                echo "✅ Convertido: $file de WINDOWS-1252 para UTF-8"
            else
                rm "${file}.temp"
                echo "❌ Falha na conversão: $file"
            fi
        fi
    fi
done