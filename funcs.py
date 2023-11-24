async def start_handler_func(message, db):
    await message.answer('Здарова заiбал')
    await db.execute("INSERT OR IGNORE INTO users_table (id) VALUES (?)", (message.from_user.id,))
    await db.commit()
