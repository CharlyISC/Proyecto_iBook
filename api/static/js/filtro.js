
    //Filtro
    function filtrarTabla() {
        var input, filter, table, tr, td, i, j, txtValue;
        input = document.getElementById("buscarInput");
        filter = input.value.toUpperCase();
        table = document.getElementById("miTabla");
        tr = table.getElementsByTagName("tr");

        for (i = 1; i < tr.length; i++) {
        tr[i].style.display = "none";
        td = tr[i].getElementsByTagName("td");
        for (j = 0; j < td.length; j++) {
            if (td[j]) {
            txtValue = td[j].textContent || td[j].innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
                break;
            }
            }
        }
        }
    }

       //Aqui exporta al excel
       function exportarExcel() {
        var tabla = document.getElementById("miTabla");
        var libro = XLSX.utils.table_to_book(tabla);
        XLSX.writeFile(libro, "tabla.xlsx");
    }

    //Eventos
    document.getElementById("buscarInput").addEventListener("keyup", filtrarTabla);
    document.getElementById("exportarExcel").addEventListener("click", exportarExcel);
