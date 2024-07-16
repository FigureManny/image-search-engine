import random

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/gifs')
def gifs():
    myGifs = [
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWpjOHliNWE0djJ0OWRpMHNmeDRvZm1wbmIyYzV5dDVtd3owZ2V0cCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B3aYrt2MEFjhsWOuNg/giphy.webp",
        "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2pibzJ0ejVqZG44OWxlYnM4aDdzd3RucW1hNWYxeW4zN3YyNGppbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6A04Tnu0LN4oN8NUBW/giphy.webp",
        "https://media2.giphy.com/media/Qw4X3FLQZZLJ4ndBcPK/giphy.webp?cid=790b7611yuoqbt5ecjko5t6c26l2yv3gm4xptvtt93vj9fef&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media2.giphy.com/media/h8rlhOTBjAIfrkWjA0/giphy.webp?cid=790b7611yuoqbt5ecjko5t6c26l2yv3gm4xptvtt93vj9fef&ep=v1_gifs_search&rid=giphy.webp&ct=g",
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWtteDZ3YTF1eG9nZTFweWVkZjN1ZjllcGJxa3dvcW5zOWp4YzVoNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/SSWDmOtwTQ3X5nNBRN/giphy.webp"
    ]
    randomGif = random.choice(myGifs)

    imgData = {
        "fcb": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2pibzJ0ejVqZG44OWxlYnM4aDdzd3RucW1hNWYxeW4zN3YyNGppbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6A04Tnu0LN4oN8NUBW/giphy.webp"
    }

    return render_template('gifs.html', randomGif=randomGif, myGifs=myGifs, imgData=imgData)

@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        query = request.form['query']
        imgData = {
            "fcb": "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2pibzJ0ejVqZG44OWxlYnM4aDdzd3RucW1hNWYxeW4zN3YyNGppbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/6A04Tnu0LN4oN8NUBW/giphy.webp"
        }
        if query not in imgData:
            return "No data found for " + query
        return render_template('gifs.html', randomGif=imgData[query], myGifs=None, imgData=imgData)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
