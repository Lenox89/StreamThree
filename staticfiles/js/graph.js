$.getJSON( '/data', function (data) {
  makeGraphs(null, data)
  function makeGraphs(error, ticketData) {
    if (error) {
      console.error("makeGraphs error on receiving dataset:", error.statusText);
      throw error;
    }

    dc.config.defaultColors(d3.schemeAccent)

    // Crossfilter
    var ndx = crossfilter(ticketData);

    // Dims
    var statusDim = ndx.dimension(function (d) {
      return d.fields.status;
    }); 

    // Groups
    var all = ndx.groupAll();
    var statusGroup = statusDim.group();

    // Graphs
    var completeNumber = dc.numberDisplay('#complete-number');
    var workingNumber = dc.numberDisplay('#working-number');
    var pendingNumber = dc.numberDisplay('#pending-number');
    var allTickets = dc.pieChart('#ticket-status');

    // Setup
    var ticketStatus = { complete: [], working: [], pending: [] } // All tickets by status

    // Get All Complete Tickets
    ticketData.forEach(function(d){ 
      // console.log(d.fields.status)
      switch (d.fields.status) {
        case 'Complete':
          ticketStatus.complete.push(d);
          break;
        case 'Working':
          ticketStatus.working.push(d);
          break;
        case 'Pending':
          ticketStatus.pending.push(d);
          break;
        default:
          console.error('There is an issue with the status type');
      }
    });

    // Complete ticket setup
    var completeCrossfilter = crossfilter(ticketStatus.complete);
    var completeAll = completeCrossfilter.groupAll();
    var completeDim = completeCrossfilter.dimension(function (d) {
      return d.type;
    });
    var completeGroup = completeDim.group();

    // Working ticket setup
    var workingCrossfilter = crossfilter(ticketStatus.working);
    var workingAll = workingCrossfilter.groupAll();
    var workingDim = workingCrossfilter.dimension(function (d) {
      return d.type;
    });
    var workingGroup = workingDim.group();

    // Pending ticket setup
    var pendingCrossfilter = crossfilter(ticketStatus.pending);
    var pendingAll = pendingCrossfilter.groupAll();
    var pendingDim = pendingCrossfilter.dimension(function (d) {
      return d.type;
    });
    var pendingGroup = pendingDim.group();

    // console.log(window.group = all)
    
    // Number diplays

    // Complete
    completeNumber
    .group(completeAll)
    .formatNumber(d3.format(".1s"))
    .valueAccessor(function(d) {
      return d;
    });

    // Working
    workingNumber
    .group(workingAll)
    .formatNumber(d3.format(".1s"))
    .valueAccessor(function(d) {
      return d;
    });

    // Pending
    pendingNumber
    .group(pendingAll)
    .formatNumber(d3.format(".1s"))
    .valueAccessor(function(d) {
      return d;
    });

    allTickets
    .dimension(statusDim)
    // .width(700)
    .emptyTitle('No Data To Display')
    // .radius(600)
    .group(statusGroup)
    .label(function (d) {
      return d.key+": "+Math.floor(d.value*100/all.value())+'%'
    })
    .ordinalColors(['#ff7f00','#ffff33','#a65628']);

    $( window ).resize(function() {
      dc.redrawAll();
      dc.renderAll();
    });

    // Renderer
    dc.renderAll();
  }
})
