css = open("styles.css").read()

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/B5dz97Jw/bot-templates.jpg" alt="bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/Xxp5SBqF/user-template.jpg" alt="user">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''