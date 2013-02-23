
var created = false

var barParent;

var svg;
var SVG_HEIGHT = 500;
var data;

var bar,
    barHeight = 76,
    barWidth,
    barTextPanel,
    barTextHover = -1,
    barTexts = [];
var BAR_DATES_SELECTED = '#fff',
    BAR_DATES_UNSELECTED = '#666',
    BAR_DATES_HOVER = '#888',
    BAR_HORIZONTAL_OFFSET = 0.0;   //percent

var TRANSITION_TIME = 450;



var dayCount,
    dayLength,
    dayFirst;

var menuWeatherColors = ["#36c", "#ff6", "#e30"];
var menuWeatherList;

var sliderContentPanel;

function createBar(parent, object, firstDate, width) {
    wList = object.map(function (d, i) {
        return d.weather;
    });
        if (created) {
            alert("createBar called twice");
            return;
        }

        //put args into globals
        dayCount = wList.length;
        barParent = parent;
        menuWeatherList = wList;
        barWidth = width;
        dayLength = width / dayCount;
        dayFirst = firstDate;
        data = object;


        //create components
        setupSvg();

        setupBar();

        //setup slider
        setupSlide();
        setupTable();
        //texts and lines
        setupTextLines();
        setupTooltip();


        TRANSITION_TIME = 0;
        moveSlider(0);
        redrawTextLines();
        TRANSITION_TIME = 450;


    //}, 200);
}

var barDiv;

var mapDiv;

function setupSvg() {
    barDiv = d3.select(barParent).append('div')
            .attr('id', 'menuDiv');

    svg = barDiv.append('svg')
        .attr('id', 'barSvg')
        .attr('width', barWidth)
        .attr('height', SVG_HEIGHT);
}

function setupBar() {
    bar = svg.append('rect')
            .attr('id', 'bar')
            .attr('width', '100%')
            .attr('height', barHeight);

    //and its gradient
    var gradientData = [];
    for (var i = 0; i < dayCount; i++) {
        var perc = (100 * (i + 0.5) / dayCount) + "%";
        var colId = Math.floor((menuWeatherList[i] * 2))
        var colRatio = (menuWeatherList[i] % 0.5) * 2;
        var color = d3.interpolate(menuWeatherColors[colId], menuWeatherColors[colId + 1])(colRatio)
        gradientData.push({ offset: perc, color: color });
    }
    svg.append("linearGradient")
        .attr("id", "barGradient")
        .attr("gradientUnits", "userSpaceOnUse")
        .attr("x1", 0).attr("y1", 0)
        .attr("x2", barWidth).attr("y2", 0)
    .selectAll("stop")
        .data(gradientData)
    .enter().append("stop")
        .attr("offset", function (d) { return d.offset; })
        .attr("stop-color", function (d) { return d.color; });
    bar.attr("fill", 'url(#barGradient)');

    //event handlers
    bar.on('mousedown', function () {

        var id = Math.floor(menuWeatherList.length * d3.mouse(this)[0] / barWidth);
        if (sliderPos != id && id >= 0 && id < dayCount) {
            sliderPos = id;
            redrawTextLines();
            moveSlider(id);
        }
    })
        .on('mousemove', function () {
            var id = Math.floor(menuWeatherList.length * d3.mouse(this)[0] / barWidth);
            if (barTextHover != id) {
                barTextHover = id;
                redrawTextLines();
            }
        })
        .on('mouseout', function () {
            barTextHover = -1;
            redrawTextLines();
        });


}

function setupTextLines() {
    var tlGroup = svg.append('g').attr('id', 'textAndLineGroup');
    for (var i = 0; i < dayCount; i++) {
        barTexts[i] = tlGroup.append('text')
            .text(getDayString(dayFirst, i))
                .attr('text-anchor', 'left')
                .attr('pointer-events', 'none')
                .style('font-weight', 'bold')
                .attr({ x: dayLength * i + dayLength * 0.6, y: barHeight / 3, fill: (i == sliderPos ? BAR_DATES_SELECTED : BAR_DATES_UNSELECTED) });
        if (i > 0)
            svg.append('line')
                .attr("x1", dayLength * i)
                .attr("y1", barHeight / 10)
                .attr("x2", dayLength * i)
                .attr("y2", barHeight * 9 / 10)
                .attr('pointer-events', 'none')
                .style("stroke", 'white')
                .style("stroke-width", 3)
                .style('stroke-opacity', 0.9);
    }
}

var barTooltip;
function setupTooltip() {
    barTooltip = barDiv.append("div")
    .attr("class", "tooltip")
    .style("opacity", 0);
}

var tipOffsetX = 12,
    tipOffsetY = 20;
function showTooltip(text, p) {
    if (p == null) {
        p = { x: d3.event.pageX + tipOffsetX, y: d3.event.pageY + tipOffsetY };
    }
    barTooltip
        .transition().duration(200)
        .style("opacity", 0.9)
        .text(text);
}

function moveTooltip() {
    barTooltip
        .style("left", (d3.event.pageX + tipOffsetX) + "px")
        .style("top", (d3.event.pageY + tipOffsetY) + "px");
}

function hideTooltip() {
    barTooltip
        .transition().duration(200)
        .style("opacity", 1e-6);
}

function addTooltip(o, f) {
    o.on('mousemove', function () {
            moveTooltip();
        })
        .on('mouseenter', function (d) {
            showTooltip(f(o));
        })
        .on('mouseout', function (d) {
            hideTooltip();
        })
}


//refreshes the colors 
function redrawTextLines() {
    for (var i = 0; i < barTexts.length; i++) {
        var col = BAR_DATES_UNSELECTED;
        if (sliderPos == i)
            col = BAR_DATES_SELECTED;
        else if (barTextHover == i)
            col = BAR_DATES_HOVER;
        if(barTexts[i].attr('fill') != col)
            barTexts[i]
                .transition().duration(150)
                .attr('fill', col);

    }
}

function getDayString(firstDate, offset)
{
    var today = new Date(firstDate + 24 * 60 * 60 * 1000 * offset);
    //return today;

    var dd = today.getDate();
    var mm = today.getMonth();
    var months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
    return dd + " " + months[mm];
}
