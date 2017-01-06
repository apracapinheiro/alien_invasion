# from distutils.core import setup
# import py2exe
#
#
# setup(console=['alien_invasion.py'])
#


import cx_Freeze

executavel = [cx_Freeze.Executable("alien_invasion.py")]

cx_Freeze.setup(
    name="Aliens Invasion by Falcon",
    version="0.0.1",
    description="O inicio para dominar o mundo dos games",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["BallBounce.wav",
                                             "ship_explosion.wav",
                                             "Zap.wav", 'images']}},
    executables=executavel




# import cx_Freeze
#
# executavel = [cx_Freeze.Executable("alien_invasion.py")]
#
# cx_Freeze.setup(
#     name="Space Invaders Falcon",
#     version="0.0.1",
#     description="O inicio para dominar o mundo dos games",
#     options={"build_exe": {"packages": ["pygame"],
#                            "include_files": ["alien.py", "BallBounce.wav", "bullet.py", "button.py",
#                                              "game_functions.py", "game_stats.py", "scoreboard.py",
#                                              "settings.py", "ship.py", "ship_explosion.wav",
#                                              "Zap.wav", 'images']}},
#     executables=executavel
)
