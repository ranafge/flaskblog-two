from app import create_app, db
import cli
from app.models import User, Post, Notification, Message

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_context_processor():
    return dict(app=app, User=User,Post=Post, db=db, Notification=Notification, Message=Message)




if __name__=="__main__":
    app.run()





