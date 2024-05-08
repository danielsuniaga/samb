# echo "START .SH"

# wait-for-it.sh database:3306 --timeout=60 --strict -- python manage.py makemigrations

# if [ $? -eq 0 ]; then

#     echo "Makemigrations completed successfully"

# else

#     echo "Error: Makemigrations failed"
#     exit 1

# fi

# wait-for-it.sh database:3306 --timeout=60 --strict -- python manage.py migrate

# if [ $? -eq 0 ]; then
#     echo "Migrate completed successfully"
# else
#     echo "Error: Migrate failed"
#     exit 1
# fi
