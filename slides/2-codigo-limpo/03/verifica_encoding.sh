# Verificar encoding de todos os arquivos
for file in examples/*; do
    if [ -f "$file" ]; then
        encoding=$(file -I "$file" | awk -F'charset=' '{print $2}')
        echo "$file: $encoding"
    fi
done