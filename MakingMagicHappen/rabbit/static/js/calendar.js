
   
;(function ( $, window, document, undefined ) {
    
	"use strict";
    // Create the defaults once
    var pluginName = "simpleCalendar",
        defaults = {
            months: ['january','february','march','april','may','june','july','august','september','october','november','december'], //string of months starting from january
            days: ['sunday','monday','tuesday','wenesday','thursday','friday','saturday'], //string of days starting from sunday
            insertEvent: false, // can insert events
            displayEvent: true, // display existing event
            fixedStartDay: true, // Week begin always by monday
            event: [], //List of event
            insertCallback : function(){} // Callback when an event is added to the calendar
        };

    // The actual plugin constructor
    function Plugin ( element, options ) {        
        this.element = element;
        this.settings = $.extend( {}, defaults, options );
        this._defaults = defaults;
        this._name = pluginName;
        this.currentDate = new Date();
        this.init();
    }

    // Avoid Plugin.prototype conflicts
    $.extend(Plugin.prototype, {
        init: function () {
            var container = $(this.element);
            var todayDate = this.currentDate;
            var calendar = $('<div class="calendar"></div>');
            var header = $('<header>'+
                           '<h4 class="month"></h4>'+
                           '<a class="btn btn-prev" href="#" style="margin-top: 10px; margin-left:10px; padding: 0px 0 10px 0;"><i class="fa fa-angle-left" ></i></a>'+
                           '<a class="btn btn-next" href="#" style="margin-top: 10px; margin-right:10px; padding: 0px 0 10px 0;"><i class="fa fa-angle-right"></i></a>'+
				            '</header>');
            
            this.updateHeader(todayDate,header);
            calendar.append(header);
            
            this.buildCalendar(todayDate,calendar);
            container.append(calendar);
            
            this.bindEvents();
        },
        
        //Update the current month header
        updateHeader: function (date, header) {
            header.find('.month').html(date.getFullYear() + '    '+this.settings.months[date.getMonth()]);
        },
        //Build calendar of a month from date
        buildCalendar: function (fromDate, calendar) {
            var plugin = this;
            
            calendar.find('table').remove();
            
            var body = $('<table></table>');
            var thead = $('<thead></thead>');
            var tbody = $('<tbody></tbody>');
            
            //Header day in a week ( (1 to 8) % 7 to start the week by monday)
            for(var i=1; i<=this.settings.days.length; i++) {
                thead.append($('<td>'+this.settings.days[i%7].substring(0,3)+'</td>'));
            }
            
            //setting current year and month
            var y = fromDate.getFullYear(), m = fromDate.getMonth();
            
            //first day of the month
            var firstDay = new Date(y, m, 1);
            //If not monday set to previous monday
            while(firstDay.getDay() != 1){
                firstDay.setDate(firstDay.getDate()-1);
            }
            //last day of the month
            var lastDay = new Date(y, m + 1, 0);
            //If not sunday set to next sunday
            while(lastDay.getDay() != 0){
                lastDay.setDate(lastDay.getDate()+1);
            }
            
            //For firstDay to lastDay
            for(var day = firstDay; day <= lastDay; day.setDate(day.getDate())) {
                var tr = $('<tr></tr>');
                //For each row
                for(var i = 0; i<7; i++) {
                    var td = $('<td><a href="#" class="day">'+day.getDate()+'</a></td>');
                    //if today is this day
                    if(day.toDateString() === (new Date).toDateString()){
                        td.find(".day").addClass("today");
                    }
                    //if day is not in this month
                    if(day.getMonth() != fromDate.getMonth()){
                       td.find(".day").addClass("wrong-month"); 
                    } 
                    tr.append(td);
                    day.setDate(day.getDate() + 1);
                }
                tbody.append(tr);
            }
            body.append(thead);
            body.append(tbody);
            
            var eventContainer = $('<div class="event-container"><a class="close" aria-hidden="true" style="align:right"> X </a>'+
                                                 '</div>');

            //event creation form
            // var eventCreation = $('<>')
           var modal = ('<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">' +
                        '<div class="modal-dialog" role="document">' +
                        '<div class="modal-content">' +
                        '<div class="modal-header">'+
                        '<h5 class="modal-title" id="exampleModalLabel">New message</h5>'+
                        '<button type="button" class="close" data-dismiss="modal" aria-label="Close">'+
                        '<span aria-hidden="true">&times;</span>'+
                        '</button>'+
                        '</div>'+
                        '<div class="modal-body">'+
                        '<form>'+
                        '<div class="form-group">'+
                        '<label for="recipient-name" class="col-form-label">Recipient:</label>'+
                        '<input type="text" class="form-control" id="recipient-name">'+
                        '</div>'+
                        '<div class="form-group">'+
                        '<label for="message-text" class="col-form-label">Message:</label>'+
                        '<textarea class="form-control" id="message-text"></textarea>'+
                        '</div>'+
                        '</form>'+
                        '</div>'+
                        '<div class="modal-footer">'+
                        '<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>'+
                        '<button type="button" class="btn btn-primary">Send message</button>'+
                        '</div>'+
                        '</div>'+
                        '</div>'+
                        '</div>')
            calendar.append(body);
            calendar.append(eventContainer);
            if(logged == 1){
                // eventContainer.append(form);
               
            }
            else{
                eventContainer.append('<div class="event"> I am  not logged in </div>');

            }
        },
        //Init global events listeners
        bindEvents: function () {
            var plugin = this;
            
            //Click previous month
            $('.btn-prev').click(function(){
                plugin.currentDate.setMonth(plugin.currentDate.getMonth()-1);
                plugin.buildCalendar(plugin.currentDate, $('.calendar'));
                plugin.updateHeader(plugin.currentDate, $('.calendar header'));
                
            });
            
            //Click next month
            $('.btn-next').click(function(){
                plugin.currentDate.setMonth(plugin.currentDate.getMonth()+1);
                plugin.buildCalendar(plugin.currentDate, $('.calendar'));
                plugin.updateHeader(plugin.currentDate, $('.calendar header'));
                
            });

            $('.td').click(function(){
                modal.open();
            })
        }
    });

    // A really lightweight plugin wrapper around the constructor,
    // preventing against multiple instantiations
    $.fn[ pluginName ] = function ( options ) {
        return this.each(function() {
                if ( !$.data( this, "plugin_" + pluginName ) ) {
                        $.data( this, "plugin_" + pluginName, new Plugin( this, options ) );
                }
        });
    };
})( jQuery, window, document );
var logged = 0;
function is_authenticate(logg){
        logged = logg;
        insertEvent= true;
}
