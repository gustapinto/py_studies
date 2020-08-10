from tasks import add

# Call the redis task
result = add.delay(4, 4)

# Check if tasks is finished or not
result.ready()
