/*
 * View model for GCode Sticky Options
 *
 * Author: jneilliii
 * License: AGPLv3
 */
$(function() {
    function GcodestickyoptionsViewModel(parameters) {
        var self = this;

        self.settingsViewModel = parameters[0];
        self.gcodeViewModel = parameters[0];

        self.onBeforeBinding = function() {
            $('#gcodestickyoptions').insertAfter('#gcode div.advanced_options button:last');
        };

        self.onAfterBinding = function() {
            // if(current === "#gcode"){
                $('#gcode input[type="checkbox"]').each(function(i, elem){
                    if(self.settingsViewModel.settings.plugins.gcodestickyoptions.checkboxes()[i] && !elem.checked){
                        console.log('clicking checkbox: ' + i);
                        $(elem).trigger('click');
                    }
                });
            //}
        };

        self.saveOptions = function() {
            self.settingsViewModel.settings.plugins.gcodestickyoptions.checkboxes($('#gcode input[type="checkbox"]').map(function(){return $(this).is(':checked');}).get());
            self.settingsViewModel.saveData();
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: GcodestickyoptionsViewModel,
        dependencies: [ "settingsViewModel", "gcodeViewModel" ],
        elements: [ "#gcodestickyoptions_button" ]
    });
});
