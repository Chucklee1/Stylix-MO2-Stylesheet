## Info:
  - This theme uses a Mustache formatted templates with Nix Stylix to allow for a MO2 theme
    that matches with your own system theme
  - The overall idea is pretty simple: Have a json file with hex-colors (no #). If you have the
    nix package manager and stylix installed, you will just declare a stylix template in your nix config like so: (example is with home-manager)
      ```nix
        home.file."/path/to/your/modorganizer2/stylesheets/Stylix.qss".source = config.lib.stylix.colors {
          template = builtins.readFile /path/to/this/repo/Stylix.qss.mustache;
          extension = ".qss";
        };
      ```
  - Otherwise, you can use the simple python script I provided in the root, just make sure to replace the defined paths
  - CURRENTLY REQUIRES "vs15" AND "Paper" icon folders (comes with MO2 so should not be an issue?)

## TODO:
  - [ ] Replace current color names with base16 names
  - [ ] Add Script for color manipulation (in order to only need base16 colors)
  - [ ] Add support for wallust
  - python script:
    - [ ] Add feature in python script to prompt for file paths, maybe use zenity for gui?
    - [ ] python script: Auto detect stylix instance and search for .config/stylix/, otherwise
          fallback to use prompted json path
    - [ ] Add support for yaml and toml formats

##  Credits/Reference:
  - Based (modifed) upon builtin vs15 Dark-Purple theme & uses icons from the paper dark theme
  - Stylix: <https://nix-community.github.io/stylix>
  - Mustache: <https://mustache.github.io>
