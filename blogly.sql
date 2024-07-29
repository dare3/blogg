You are now connected to database "kemre" as user "kemre".
eate all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # If tables already exist, empty them
    User.query.delete()
    Post.query.delete()

    # Add users
    user1 = User(first_name="John", last_name="Doe", image_url="https://example.com/johndoe.jpg")
    user2 = User(first_name="Jane", last_name="Smith", image_url="https://example.com/janesmith.jpg")

    db.session.add_all([user1, user2])
    db.session.commit()

    # Add posts
    post1 = Post(title="My first post", content="This is the content of my first post", user_id=user1.id)
    post2 = Post(title="Another post", content="Here's some more content", user_id=user2.id)

    db.session.add_all([post1, post2])
    db.session.commit()
