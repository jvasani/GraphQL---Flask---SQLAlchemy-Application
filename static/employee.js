var data = allEmployee;


data = JSON.stringify(data);
data = data.replace(/\n/g, '');
data = data.replace(/\\/g, '');
data = data.replace(/\["/g, '[');
data = data.replace(/\"]/g, ']');
data = data.replace(/\}"/g, '}');
data = data.replace(/\"{/g, '{');
data = JSON.parse(data);
//data = JSON.stringify(data);
console.log(data);

    $(document).ready(function () {
        $('#list').DataTable({
            "pagingType": "full_numbers",
            "bJQueryUI":true,
            "bPaginate":true,
            "data": data,
            dom: "<'row'<'col-sm-3'l><'col-sm-3'f><'col-sm-6'p>>" +
                 "<'row'<'col-sm-12'tr>>" +
                 "<'row'<'col-sm-5'i><'col-sm-7'p>>",
            columnDefs: [
            {
                targets: [ 0, 1, 2 ],
                className: 'mdl-data-table__cell--non-numeric'
            }
           ],
            "columns": [
                {"data": "id"},
                {"data": "name"},
                {"data": "department"},
                {"data": "salary"}
            ]
        });
    });