const NODE_RADIUS = 50;
const GENERATION_GAP = 500;
const WIDTH = (window.innerWidth > 0) ? window.innerWidth : screen.width;
const HEIGHT = (window.innerHeight > 0) ? window.innerHeight : screen.height;

// set the dimensions and margins of the graph
const width = WIDTH;
const height = HEIGHT;

// append the svg object to the body of the page
var svg = d3.select("#family_tree")
    .append("svg")
    .attr("width", width)
    .attr("height", height)


// create a container to allow zooming/panning
const group = svg.append("g")

// allow zooming on the svg element
svg.call(d3.zoom().on("zoom", (event) => {
    group.attr("transform", event.transform);
}));


d3.json("../data/tree.json").then(function(data) {
    console.log(data);

    // Initialize the links
    var parent_child_link = group
        .selectAll(".parent_child_link")
        .data(data.parent_child_links)
        .attr("class", "parent_child_link")
        .join("line")
        .style("stroke", "lightblue")
        .style("stroke-width", 2)

    var partner_link = group
        .selectAll(".partner_link")
        .data(data.partner_links)
        .attr("class", "partner_link")
        .join("line")
        .style("stroke", "pink")
        .style("stroke-width", 2)

    // Initialize the nodes
    var node = group
        .selectAll("circle")
        .data(data.nodes)
        .join("circle")
        .attr("r", NODE_RADIUS)
        .style("fill", "#69b3a2")

    var label = group
        .selectAll("text")
        .data(data.nodes)
        .join("text")
        .text(d => d.name)
        .attr("text-anchor", "middle")
        .attr("font-size", 10)

    // Let's list te force we wanna apply on the network
    var simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink()
            .id(d => d.idx)
            .links(data.parent_child_links)
            .distance(GENERATION_GAP)
            .strength(0))
        .force("link", d3.forceLink()
            .id(d => d.idx)
            .links(data.partner_links)
            .distance(NODE_RADIUS * 2.25)
            .strength(0.8))
        .force("charge", d3.forceManyBody()
            .strength(-0.6)
            .distanceMin(NODE_RADIUS * 1.15)
            .distanceMax(GENERATION_GAP))
        .force("x", d3.forceX(d => d.targ_x * NODE_RADIUS * 5)
            .strength(0.1))
        .force("y", d3.forceY(d => d.gen * GENERATION_GAP)
            .strength(1))
        //.force("collide", d3.forceCollide(NODE_RADIUS * 1.15)
        //    .strength(0))
        .on("tick", ticked);


    // add drag for nodes (and labels for ease of use)
    node.call(d3.drag()
        .on("start", dragStart)
        .on("drag", dragged)
        .on("end", dragEnd));

    label.call(d3.drag()
        .on("start", dragStart)
        .on("drag", dragged)
        .on("end", dragEnd));

    function dragStart(event) {
        simulation.alphaTarget(0.5).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }

    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }

    function dragEnd(event) {
        simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }

    function ticked() {
        parent_child_link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => (d.source.p1 && d.source.p2) ? (data.nodes.find(node => node.idx == d.source.p1).x + data.nodes.find(node => node.idx == d.source.p2).x) / 2 : d.target.x)
            .attr("y2", d => (d.source.p1 && d.source.p2) ? (data.nodes.find(node => node.idx == d.source.p1).y + data.nodes.find(node => node.idx == d.source.p2).y) / 2 : d.target.y);

        partner_link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        label
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    }
});
