# NextPass - Generate Your Next Password

NextPass generates passwords in a cryoptographically secure way. 

## Usage: 
    python nextpass.py [options]

## Examples

password with the length of 10 (default is 8)

    python nextpass.py 10


password with the minimum and maximum length

    python nextpass.py 8 15

specify charset to use: lowercase (l), numeric characters (n), special symbols (s)

    python nextpass.py lns 12 15
