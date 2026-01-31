project = 'Awesome sphinx-revealjs'
copyright = '2026, Tetsuo Koyama'
author = 'Tetsuo Koyama'

extensions = [
    'sphinx_revealjs',
    'atsphinx.stlite',
]

html_theme = 'sphinx_revealjs'

revealjs_static_path = ['_static']
revealjs_style_theme = 'black'
revealjs_script_conf = {
    'controls': True,
    'progress': True,
    'history': True,
    'center': True,
    'transition': 'slide',
}

# Stlite configuration - increase display height
stlite_config = {
    'height': '600px',
}
