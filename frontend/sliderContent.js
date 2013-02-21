var contentPalette = ['#6ff', '#ff6', '#f6f', '#66f', '#6f6', '#f66'];
var contentShufflePalette = true;

var contentShown = false,
    contentGroup,
    contentHovered = false,
    contentLen,
    contentW,
    contentH;

var contentData;

var contentExpanded = false;



function setupContent() {
    contentGroup = svg.append('g')
            .attr("transform", "translate(" + (CONTENT_OFFSET * dayLength) + ",0)")
            .append('g');
}

//shows the data for a given day (schedule, width, height)
function showContent(schedule, w, h) {
    if (contentShown) {
        alert('content already shown!');
        return;
    }
    contentShown = true;

    contentW = w;
    contentH = h;

    if (contentShufflePalette)
        contentPalette = shuffle(contentPalette);

    //sliderContentPanel.
    //    style('height', barHeight * 0.4);

    contentGroup
            .attr("transform", "translate(" + (sliderPos * dayLength) + "," + (barHeight * 0.50) + ")")

    var contentPath = [{ "x": 0, "y": 0 }, { "x": 0, "y": 1 },
        { "x": 1, "y": 1 }, { "x": 1, "y": 0 }
    ];

    //format: text - size - position
    var day = schedule.slice(0);
    day = day.map(function (d, i) {
        return [d[0], d[1], 0];
    });
    for (var i = 1; i < day.length; i++)
        day[i][2] = day[i - 1][1] + day[i - 1][2];
    contentLen = day[day.length - 1][1] + day[day.length - 1][2];

    contentData = day;

    //alert(day);
    //alert(loc);
    //var START_SPREAD = 
    var lineFunction = d3.svg.line()
                             .x(function (d, i) { return d.x; })
                             .y(function (d, i) { return d.y; });


    //for each activity
    for (var i = 0; i < day.length; i++) {
        cp = contentPath.map(function (d) {
            return {
                x: d.x * w * (day[i][1] / contentLen),
                y: d.y * h
            };

        });
        var ev_id = i;
        //create paths
        var tmp = contentGroup.append('path')
            .data(cp)
            .attr("d", lineFunction(cp))
            .attr('transform', 'translate(' + (w * day[i][2] / contentLen) + ', 0)')
            .attr('fill', function (d) { return d3.rgb(contentPalette[i]).darker(1.015); })
            .attr('opacity', 1)

            .datum(i)
            .on('mousemove', function() {
                moveTooltip();
            })
            .on('mouseenter', function (d) {
                contentHovered = true;
                contentGroup.selectAll('path').attr('fill', function (d, id) { return sliderGetColor(id); })
                showTooltip('wsup');
            })
            .on('mouseout', function (d) {
                contentHovered = false;
                contentGroup.selectAll('path').attr('fill', function (d, id) { return sliderGetColor(id) });
                hideTooltip();
            })
            .on('click', function (d) {
                expandContent(d);
                contentGroup.selectAll('path').attr('fill', function (d, id) { return sliderGetColor(id) });
            })
            .attr('fill', function (d) { return contentPalette[i]; })
        //.attr("d", function (d) {
        //    return line(d.map(function (d) {
        //        return d;
        //    }))
        //});
        //alert(tmp.attr.d);
    }


}

function hideContent(after) {
    if (!contentShown)
        return;
    if (tableShown) {
        hideTable();
    }
    contentExpanded = false;
    contentHover = false;

    //sliderContentPanel
    //    //.transition().duration(100)
    //            .attr('height', '0');

    contentGroup.selectAll('path')
        .attr('position', 'absolute')
        .transition().duration(250)
        .attr('opacity', 0)
    .each('end', function()
    {
        contentGroup.selectAll('path').remove();
    });
    contentShown = false;
}

function expandContent(id) {
    contentExpanded = !contentExpanded;
    if (contentExpanded)
        showTable(contentData, (sliderPos + CONTENT_OFFSET) * dayLength, barHeight / 2 + contentH - 1, contentW, (CONTENT_OFFSET * dayLength), barHeight * 2, barWidth * 0.7);
    else
        hideTable();
}


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