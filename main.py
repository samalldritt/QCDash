import dash
from data.data_loader import Loader
from app.layout import Layout
from app.callbacks import register_callbacks

if __name__ == '__main__':
    loader = Loader()
    df = loader.get_data()
    app = dash.Dash(__name__)
    app.scripts.config.serve_locally = True
    app.css.config.serve_locally = True
    layout = Layout(df)
    app.layout = layout.create_layout()
    register_callbacks(app, df)
    app.run_server(debug=True)
