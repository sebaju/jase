<p align="center">
<img src="https://cdn.discordapp.com/attachments/816525961994567741/853912012995297299/getgud.png">
</p>
<p align="center">
he do be saving lives doe
</p>

<h1 align="center">
Jase
</h1>

**Minecraft overlay generator written in python.**

## Table of Contents

- [Overview](#overview)
- [Usage](#usage)
- [TODO](#todo)
- [More](#more)

## Overview
Generates an overlay with **seamless textures** and a **height limit discoloring** for red, blue, and white stained clay based on a configuration file. The block designs are simplistic, only having an outline and a fill color for above and below a set height. All of which are configurable for the listed clay colors. Currently there are `12` configurable colors.

## Usage
1. Install requirements using: 
 
`$ pip -r requirements.txt`  

2. Configure `conf.txt` (and optionally `jasrc/config.py`)

3. Run Jase with:  

`$ python jase.py`

### Args
`-h OR --help` Display the help message.  
`-c OR --config [CONFIGFILE]`Use a config other than the default (conf.txt).  
`-m OR --minecraft` Output the resulting zip to the (.minecraft) dir defined in your configuration.  
`-v OR --verbose` For verbosity.

## TODO
- Support for all clay colors.
- Texturing overlay using alpha.
- Seamless generator using quadrants/9 segment sample textures for more seamless textures.
- More confugurable color channels.
- Better config

## More

- SLOC: `338`
- Color channels: `2`
- Customizable colors: `12`
