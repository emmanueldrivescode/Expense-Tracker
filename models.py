from datetime import datetime

# -----  Item Creation Function -------
def create_item(item_id, description, amount, category):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

    item = {
        "ID" : item_id,
        "Description" : description,
        "Category" : category,
        "Amount" : amount,
        "Created Date" : current_time,
        "Updated Date" : current_time
    }

    return item