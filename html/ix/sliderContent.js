var contentPalette = ['#66f', '#6f6', '#f66', '#6ff', '#ff6', '#f6f'];
var contentShufflePalette = false;

var contentShown = false,
    contentPanel,
    contentHovered = false,
    contentLen,
    contentW,
    contentH;

var contentData;

var contentExpanded = false;



function setupContent() {
    contentPanel = sliderPanel.append('g')
            .attr("transform", "translate(" + (CONTENT_OFFSET * dayLength) + "," + (barHeight * 0.50) + ")")
            .append('g');
}

//shows the data for a given day (schedule, width, height)
//gets its values from menu.js
function showContent(daySchedule, w, h) {

    //alert(daySchedule);
    contentW = w;
    contentH = h;

    if (contentShufflePalette)
        contentPalette = shuffle(contentPalette);


    var contentPath = [{ "x": 0, "y": 0 }, { "x": 0, "y": 1 },
        { "x": 1, "y": 1 }, { "x": 1, "y": 0 }
    ];

    contentLen = daySchedule.path[daySchedule.path.length - 1].position + daySchedule.path[daySchedule.path.length - 1].size;

    //for each route
    var content = contentPanel.selectAll('rect.content')
        .data(daySchedule.path);
    content.enter()
        .append('rect')
        .attr('class', 'content')
        .attr('height', h)
        .attr("transform", function (d, i) {
            return "translate(" + ((i != 0) ? w : 0) + ", 0)"
        })
        .on('mousemove', function () {
            moveTooltip();
        })
        .on('mouseenter', function (d) {
            contentHovered = true;
            content.attr('fill', function (d, i) { return sliderGetColor(i); })
            showTooltip(d.name);
        })
        .on('mouseout', function (d) {
            contentHovered = false;
            content.attr('fill', function (d, i) { return sliderGetColor(i); })
            hideTooltip();
        })

    content.exit()
        .remove();

    content
        .transition().duration(TRANSITION_TIME)
        .attr('fill', function (d, i) { return sliderGetColor(i); })
        .attr('width', function (d, i) {
            return w * d.size / contentLen;
        })
        .attr("transform", function (d, i) {
            return "translate(" + w * d.position / contentLen + ", 0)"
        });


    showTable(daySchedule.path, (sliderPos + CONTENT_OFFSET) * dayLength, barHeight / 2 + contentH - 1, contentW, (CONTENT_OFFSET * dayLength), barHeight * 2, barWidth * 0.6);

}

//function hideContent(after) {
//    if (!contentShown)
//        return;
//    //if (tableShown) {
//    //    hideTable();
//    //}
//    contentExpanded = false;
//    contentHover = false;

//    //sliderContentPanel
//    //    //.transition().duration(100)
//    //            .attr('height', '0');

//    contentPanel.selectAll('path')
//        .attr('position', 'absolute')
//        .transition().duration(250)
//        .attr('opacity', 0)
//    .each('end', function()
//    {
//        contentPanel.selectAll('path').remove();
//    });
//    contentShown = false;
//}

//function expandContent() {
//    //contentExpanded = !contentExpanded;
//    //if (contentExpanded)
//        showTable(contentData, (sliderPos + CONTENT_OFFSET) * dayLength, barHeight / 2 + contentH - 1, contentW, (CONTENT_OFFSET * dayLength), barHeight * 2, barWidth * 0.7);
//    //else
//    //    hideTable();
//}


function shuffle(o) {
    for (var j, x, i = o.length; i; j = parseInt(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
    return o;
};

var sliderGetColor = function (i) {
    if (contentExpanded)
        return d3.rgb(contentPalette[i]).brighter(1.02);
    //if(!contentHovered)
    //    return d3.rgb(contentPalette[i]).darker(1.015);
    return contentPalette[i];
}