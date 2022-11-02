copied the bones from pet watch

what data type for table models? for content `db.Text` resource <a href="https://docs.sqlalchemy.org/en/14/core/type_basics.html">here</a> 

building the login section, i created an auth.txt file with my hashed pw so that I can restrict registration to just myself. i'm using the UserMixin from flask for the User class, and I'm putting my admin user in the database just so that I can set up relationships to posts and comments. the comment relationshiop is the real important one. I want to have the option to have people leave anyonymous/guest comments, and also for me to be able to leave response comments, and in order for my authorship to show up properly on those comments I make, I need the db relationship of user->comment. 

so upon successful registration, i want to see some confirmation. so when i register i am redirected to my homepage, and I want to see a message flashed saying 'successful registration, welcome myshkins'. Similarly i need the same to happen for successful login. gotta connect the flash message, current_user.is_active, and jinja templates.

the new post page, essentially the same as the registration page, but styled differently.
gotta work out the orm relationships for posts and comments. 