let workspace = null;               // Inits blockly workspace
document.body.style.opacity = 0;    // Default opacity

window.addEventListener('load', () => {

    // Document variables, must be modified if any changes are made to the index.html document related to these elements
    const blocklyArea = document.getElementById('blocklyArea'); // Blockly's Area identifier
    const blocklyDiv = document.getElementById('blocklyDiv');   // Blockly's Div identifier
    const toolbox = document.getElementById('toolbox');         // Blockly's Toolbox identifier

    //==================================================================================================================

    // Main blockly initializer
    workspace = Blockly.inject('blocklyDiv', {
        toolbox: document.getElementById('toolbox'),
        
        // Switch these true or false to enable or disable blockly properties
        scrollbars: true,       // Horizontal or vertical scrollbars
        trashcan: true,         // Trashcan (duh)

        zoom :                  //============Zooming properties=============
        {
            controls: true,     // Enables zooming controls
            wheel: true,        // Makes use of the mouse's scroll wheel to zoom
            startScale: 1.0,    // Default zooming coefficient
            maxScale: 2,        // Max zooming coefficient
            minScale: 0.5,      // Min zooming coefficient

        },                      //===========================================
        
        move :                  //============Movement properties=============
        {
            scrollbars: true,   // Horizontal or vertical scrollbars
            drag: true,         // Enables dragging
            wheel: true,        // Makes use of the mouse's scroll wheel to move

        }                       //============================================
    });

    // Adaptive resizing function
    const onResize = () => {
        blocklyDiv.style.width = blocklyArea.offsetWidth + 'px';
        blocklyDiv.style.height = blocklyArea.offsetHeight + 'px';
        Blockly.svgResize(workspace);
    };

    window.addEventListener('resize', onResize, false);
    onResize();

    // Smooth opening animation
    setTimeout( () => {
        document.body.style.transition = "opacity 0.5s";
        document.body.style.opacity = 1;
    }, 100); // Time in miliseconds
})