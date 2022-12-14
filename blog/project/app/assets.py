"""flask compile assets module"""
from flask import current_app as app
from flask_assets import Bundle


def compile_assets(assets):
    """flask compile assets function"""
    assets.autobuild = True
    assets.debug = False
    main_style_bundle = Bundle(
        'src/css/*.css',
        filters='cssmin',
        output='dist/css/style.css',
        extra={"rel": "stylesheet/css"}
    )
    main_js_bundle = Bundle(
        'src/js/*.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )

    home_style_bundle = Bundle(
        'src/css/*.css',
        'home_bp/home.css',
        filters='cssmin',
        output='dist/css/home.css',
        extra={'rel': 'stylesheet/css'}
    )

    home_js_bundle = Bundle(
        'home_bp/home.js',
        filters='jsmin',
        output='dist/js/home.min.js'
    )

    auth_style_bundle = Bundle(
        'src/css/*.css',
        'auth_bp/auth.css',
        filters='cssmin',
        output='dist/css/auth.css',
        extra={'rel': 'stylesheet/css'}
    )

    auth_js_bundle = Bundle(
        'auth_bp/auth.js',
        filters='jsmin',
        output='dist/js/auth.min.js'
    )

    posts_style_bundle = Bundle(
        'src/css/*.css',
        'posts_bp/posts.css',
        filters='cssmin',
        output='dist/css/posts.css',
        extra={'rel': 'stylesheet/css'}
    )

    posts_js_bundle = Bundle(
        'posts_bp/posts.js',
        filters='jsmin',
        output='dist/js/posts.min.js'
    )

    resources_style_bundle = Bundle(
        'src/css/*.css',
        'resources_bp/resources.css',
        filters='cssmin',
        output='dist/css/resources.css',
        extra={'rel': 'stylesheet/css'}
    )

    resources_js_bundle = Bundle(
        'resources_bp/resources.js',
        filters='jsmin',
        output='dist/js/resources.min.js'
    )

    assets.register('main_style_bundle', main_style_bundle)
    assets.register('main_js_bundle', main_js_bundle)
    assets.register('home_style_bundle', home_style_bundle)
    assets.register('home_js_bundle', home_js_bundle)
    assets.register('resources_style_bundle', resources_style_bundle)
    assets.register('resources_js_bundle', resources_js_bundle)
    assets.register('auth_style_bundle', auth_style_bundle)
    assets.register('auth_js_bundle', auth_js_bundle)
    assets.register('posts_style_bundle', posts_style_bundle)
    assets.register('posts_js_bundle', posts_js_bundle)
    if app.config['FLASK_DEBUG'] == 'true':
        main_style_bundle.build()
        home_style_bundle.build()
        home_js_bundle.build()
        resources_style_bundle.build()
        resources_js_bundle.build()
        auth_style_bundle.build()
        auth_js_bundle.build()
        posts_style_bundle.build()
        posts_js_bundle.build()
    return assets
