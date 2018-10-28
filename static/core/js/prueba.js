$(document).ready(function (){
    $.ajax({
        method: "GET",
        url: "/persona",
        dataType: 'json',
        beforeSend: function(){
            swal({
                title: "Cargando"
            });
        },
        success: function (data) {
            alertify.success('Carga completa AJAX');
            swal.close()
            console.log(data)
            labelsa = data.labels
            var ctx = document.getElementById("myChart").getContext('2d');
            $("#grafico").show();
                var myChart = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labelsa,
                    datasets: data.datos,
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero:true
                            }
                        }]
                    }
                }
            });
        },
        error: function (error_data) {
            console.log("ERROR")
        }
    });
});

