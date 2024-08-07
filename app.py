from quart import Quart, request, jsonify, render_template

app = Quart(
    __name__,
    static_folder='src/static',
    template_folder='src/templates',
    )

@app.route('/')
async def home():
    
    try:
        
        return await render_template('index.html')
    except Exception as error:
        return jsonify({'error': str(error)})