from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField , PasswordField , BooleanField , ValidationError
from wtforms.validators import DataRequired, EqualTo ,  length
from yt import vid_download
app = Flask(__name__)

app.config["SECRET_KEY"] = "nanashi@7011"

class download_form(FlaskForm):
    link = StringField("Youtube Link" , validators=[DataRequired()])

    submit = SubmitField("Download") 


@app.route('/',methods=['GET','POST'])
def hello_world():
    link = None
    form = download_form()
    if form.validate_on_submit():
        link =  form.link.data
        vid_down = vid_download(link)
        vid_down.download()
        form.link.data =  ''
        if "youtube" not in link:
            return render_template("error.html",)
        else:
            return render_template ('download_page.html', form=form, link=link)
        
    else:
        return render_template('index.html', form=form, link=link)

@app.route('/download')
def download():
    return render_template('download_page.html')


if __name__ == "__main__":
    app.run(debug=True)