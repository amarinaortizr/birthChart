$(document).ready(function () {
    // Objeto para llevar un registro de si cada input ha sido modificado
    const inputState = {};

    function setupAutocomplete(inputId, resultsId) {
        const input = $(`#${inputId}`);
        const results = $(`#${resultsId}`);
        let selectedIndex = -1; // Índice para la navegación con teclado

        // Inicializa el estado del campo
        inputState[inputId] = { isSelected: false, value: "" };

        // Al escribir en el input, mostrar resultados de autocompletado
        input.on("input", function () {
            const query = $(this).val();
            inputState[inputId].isSelected = false; // Resetear la bandera cuando el usuario escribe
            inputState[inputId].value = query; // Actualiza el valor que el usuario está escribiendo
            if (query.length > 0) {
                $.get("/autocomplete", { q: query }, function (data) {
                    results.empty(); // Limpia resultados previos
                    selectedIndex = -1; // Reinicia el índice
                    data.forEach(function (word) {
                        results.append(`<li>${word}</li>`);
                    });
                    results.show(); // Muestra el dropdown cuando hay resultados
                });
            } else {
                results.empty(); // Vacía si no hay texto
                results.hide(); // Oculta el dropdown cuando no hay texto
            }
        });

        // Al hacer clic en el input, cargar todos los resultados
        input.on("focus", function () {
            if (!inputState[inputId].isSelected) { // Solo cargar todos los resultados si no se ha seleccionado nada
                $.get("/autocomplete", function (data) {
                    results.empty(); // Limpia resultados previos
                    selectedIndex = -1; // Reinicia el índice
                    data.forEach(function (word) {
                        results.append(`<li>${word}</li>`);
                    });
                    results.show(); // Muestra todos los resultados cuando se hace clic
                });
            }

            // Borrar el contenido de los otros inputs si no se han seleccionado
            $(".autocomplete input").not(this).each(function () {
                const id = $(this).attr("id");
                if (!inputState[id].isSelected) {
                    $(this).val(""); // Borra el contenido si no se seleccionó nada
                }
            });

            // Cerrar los dropdowns de los demás campos
            $(".autocomplete-results").empty().hide();
        });

        // Navegar con las flechas del teclado
        input.on("keydown", function (e) {
            const items = results.children("li");
            if (e.key === "ArrowDown") {
                e.preventDefault();
                if (selectedIndex < items.length - 1) {
                    selectedIndex++;
                    updateHighlight(items);
                }
            } else if (e.key === "ArrowUp") {
                e.preventDefault();
                if (selectedIndex > 0) {
                    selectedIndex--;
                    updateHighlight(items);
                }
            } else if (e.key === "Enter") {
                e.preventDefault();
                if (selectedIndex >= 0 && selectedIndex < items.length) {
                    input.val($(items[selectedIndex]).text());
                    results.empty();
                    results.hide(); // Oculta el dropdown al seleccionar
                    inputState[inputId].isSelected = true; // Marca que se seleccionó una opción
                }
            }
        });

        // Al hacer click en una opción del dropdown
        results.on("click", "li", function () {
            input.val($(this).text());
            results.empty();
            results.hide(); // Oculta el dropdown después de hacer la selección
            inputState[inputId].isSelected = true; // Marca que se seleccionó una opción
        });

        // Función para actualizar la opción resaltada
        function updateHighlight(items) {
            items.removeClass("highlighted");
            if (selectedIndex >= 0 && selectedIndex < items.length) {
                $(items[selectedIndex]).addClass("highlighted");
            }
        }

        // Cerrar el dropdown cuando se hace clic fuera de él
        $(document).on("click", function (e) {
            if (!$(e.target).closest(`#${inputId}, #${resultsId}`).length) {
                results.empty();
                results.hide();
            }
        });

        // Borrar el contenido del input cuando se hace clic en otro recuadro, solo si no se seleccionó una opción
        input.on("focus", function () {
            // Si no se seleccionó una opción en el campo actual y el valor no ha cambiado, borrar el contenido
            if (!inputState[inputId].isSelected && inputState[inputId].value !== input.val()) {
                input.val(""); // Borra el contenido del input si no fue seleccionado previamente
            }
        });
    }

    // Configurar autocompletado para cada fila de manera dinámica
    $(".autocomplete input").each(function (index) {
        const inputId = $(this).attr("id");
        const resultsId = `autocomplete-results-${index + 1}`;
        setupAutocomplete(inputId, resultsId);
    });
});
