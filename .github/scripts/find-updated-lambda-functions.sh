changed_func_files=()

func_files=($(ls src/lambda_functions/*.py))
for file in "${func_files[@]}"
do
    if [[ ${ALL_CHANGED_FILES[@]} =~ $file ]]
    then
        changed_funcs+=($file)
    fi
done

num="${#changed_funcs[@]}"
echo $changed_funcs
echo ${changed_funcs[@]}


echo "updated_funcs=${changed_funcs[@]}" >> $GITHUB_OUTPUT
echo "updated_funcs_count=${num}" >> $GITHUB_OUTPUT