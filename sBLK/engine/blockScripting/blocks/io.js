// IO Blocks

Blockly.defineBlocksWithJsonArray([
    //=========print("Message")============
    {
        "type": "io_print",
        "message0": "print %1 to console",
        "args0": 
        [
            {
                "type": "input_value",
                "name": "TEXT",
                "check": "String"
            }
        ],

        "previousStatement": null,
        "nextStatement": null,
        "colour": "#2980B9",
        "tooltip": "Prints text in the console",
        "helpUrl": ""
    }
]);