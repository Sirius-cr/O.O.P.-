document.addEventListener('DOMContentLoaded', function() {
    
    // =========================================================================
    // NAVEGACIÓN POR PESTAÑAS (TABS)
    // =========================================================================
    const tabButtons = document.querySelectorAll('.nav-tab-btn');
    const tabPanes = document.querySelectorAll('.tab-pane');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');
            localStorage.setItem('activeTab', targetTab);

            // Quitar clase activa de botones
            tabButtons.forEach(btn => btn.classList.remove('active'));
            // Quitar clase activa de paneles
            tabPanes.forEach(pane => pane.classList.remove('active'));

            // Activar botón actual y su correspondiente panel
            button.classList.add('active');
            const activePane = document.getElementById(targetTab);
            if (activePane) {
                activePane.classList.add('active');
            }
        });
    });

    // Restaurar pestaña activa
    const savedTab = localStorage.getItem('activeTab');
    if (savedTab) {
        const btnToClick = document.querySelector(`.nav-tab-btn[data-tab="${savedTab}"]`);
        if (btnToClick) {
            btnToClick.click();
        }
    }

    // =========================================================================
    // DROPDOWN DE USUARIO Y NOTIFICACIONES (TOGGLE)
    // =========================================================================
    const btnUsuario = document.getElementById('btn-usuario');
    const userDropdown = document.getElementById('user-dropdown-menu');
    const btnNotif = document.getElementById('btn-notificaciones');
    const notifDropdown = document.getElementById('notif-dropdown-menu');

    if (btnUsuario && userDropdown) {
        btnUsuario.addEventListener('click', (e) => {
            e.stopPropagation();
            userDropdown.classList.toggle('active');
            if (notifDropdown) notifDropdown.classList.remove('active');
        });

        document.addEventListener('click', (e) => {
            if (!userDropdown.contains(e.target) && e.target !== btnUsuario) {
                userDropdown.classList.remove('active');
            }
        });
    }

    if (btnNotif && notifDropdown) {
        btnNotif.addEventListener('click', (e) => {
            e.stopPropagation();
            notifDropdown.classList.toggle('active');
            if (userDropdown) userDropdown.classList.remove('active');
        });

        document.addEventListener('click', (e) => {
            if (!notifDropdown.contains(e.target) && e.target !== btnNotif) {
                notifDropdown.classList.remove('active');
            }
        });
    }

    window.marcarLeidas = function() {
        fetch('/student/mark_notifications_read', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Quitar badge
                const badge = btnNotif.querySelector('.notification-badge');
                if (badge) badge.remove();
                
                // Actualizar estilos en la lista
                const listItems = notifDropdown.querySelectorAll('#notif-list > div');
                listItems.forEach(item => {
                    item.style.borderLeftColor = 'var(--card-border)';
                    item.style.background = 'rgba(0, 0, 0, 0.02)';
                    const p = item.querySelector('p');
                    if (p) {
                        p.style.color = 'var(--text-secondary)';
                        p.style.fontWeight = 'normal';
                    }
                });
                
                // Ocultar botón de marcar leídas
                const btnMarcar = notifDropdown.querySelector('button');
                if (btnMarcar) btnMarcar.remove();
                
                showNotification("Notificaciones marcadas como leídas", "success");
            }
        })
        .catch(err => console.error("Error al marcar notificaciones como leídas:", err));
    };

    // =========================================================================
    // MODALES (ABRIR Y CERRAR)
    // =========================================================================
    window.openModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.add('active');
        }
    };

    window.closeModal = function(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('active');
            if (modalId === 'modal-view-report' && window.shouldReloadOnCloseReport) {
                window.shouldReloadOnCloseReport = false;
                window.location.reload();
            }
        }
    };

    // Cerrar modal haciendo clic fuera de la caja
    const modals = document.querySelectorAll('.modal-overlay');
    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
                if (modal.id === 'modal-view-report' && window.shouldReloadOnCloseReport) {
                    window.shouldReloadOnCloseReport = false;
                    window.location.reload();
                }
            }
        });
    });

    // =========================================================================
    // SECCIÓN DOCENTE: SELECCIÓN DE MATERIA/SECCIÓN
    // =========================================================================
    const sectionItems = document.querySelectorAll('.section-item-card');
    const sectionTables = document.querySelectorAll('.section-students-table');

    if (sectionItems.length > 0) {
        sectionItems.forEach(item => {
            item.addEventListener('click', () => {
                const sectionId = item.getAttribute('data-section-id');

                // Cambiar clase activa en sidebar
                sectionItems.forEach(i => i.classList.remove('active'));
                item.classList.add('active');

                // Mostrar la tabla correspondiente
                sectionTables.forEach(table => {
                    if (table.getAttribute('data-section-id') === sectionId) {
                        table.style.display = 'block';
                    } else {
                        table.style.display = 'none';
                    }
                });
            });
        });
        
        // Activar la primera sección por defecto al cargar
        sectionItems[0].click();
    }

    // =========================================================================
    // PETICIÓN AJAX: FORMULARIOS DE NOTAS (DOCENTE)
    // =========================================================================
    window.saveGrades = function(studentId, sectionId) {
        const row = document.getElementById(`row-${studentId}`);
        if (!row) return;

        const p1 = row.querySelector('.p1-input').value;
        const p2 = row.querySelector('.p2-input').value;
        const asistencia = row.querySelector('.asistencia-input').value;

        const formData = new FormData();
        formData.append('estudiante_id', studentId);
        formData.append('seccion_id', sectionId);
        formData.append('parcial1', p1);
        formData.append('parcial2', p2);
        formData.append('asistencia', asistencia);

        fetch('/teacher/save_grades', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                // Calcular y mostrar promedio localmente en la tabla
                const n1 = parseFloat(p1) || 0;
                const n2 = parseFloat(p2) || 0;
                const finalGrade = (n1 + n2) / 2;
                
                row.querySelector('.final-grade-cell').textContent = finalGrade.toFixed(2);
                
                // Mostrar alerta flotante o indicador
                showNotification(data.message, 'success');
                
                // Recargar dashboard suavemente después de 1 segundo si es necesario, o dejarlo dinámico
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(err => {
            console.error('Error al guardar notas:', err);
            showNotification('Error de conexión al guardar calificaciones.', 'error');
        });
    };

    // =========================================================================
    // PETICIÓN AJAX: GENERAR REPORTES (ESTUDIANTE Y DOCENTE)
    // =========================================================================
    
    // Estudiante: Solicitar Certificado
    const reqCertForm = document.getElementById('form-request-certificate');
    if (reqCertForm) {
        reqCertForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/student/request_certificate', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const consoleContent = document.getElementById('report-console-content');
                    if (consoleContent) {
                        consoleContent.textContent = data.report_content;
                        openModal('modal-view-report');
                        window.shouldReloadOnCloseReport = true;
                    }
                    showNotification(data.message, 'success');
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // Estudiante: Solicitar Retiro
    const reqWithdrawForm = document.getElementById('form-request-withdrawal');
    if (reqWithdrawForm) {
        reqWithdrawForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/student/request_withdrawal', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification(data.message, 'success');
                    closeModal('modal-withdraw');
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // Docente: Realizar Reporte General
    const docReportForm = document.getElementById('form-docente-report');
    if (docReportForm) {
        docReportForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/teacher/generate_report', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const consoleContent = document.getElementById('report-console-content');
                    if (consoleContent) {
                        consoleContent.textContent = data.report_content;
                        openModal('modal-view-report');
                        window.shouldReloadOnCloseReport = true;
                    }
                    showNotification(data.message, 'success');
                    closeModal('modal-create-report');
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // =========================================================================
    // PETICIÓN AJAX: ACCIONES DE COORDINADOR
    // =========================================================================

    // Iniciar/Finalizar Período
    window.togglePeriod = function(action) {
        const formData = new FormData();
        formData.append('accion', action);

        fetch('/coordinator/toggle_period', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showNotification(data.message, 'success');
                setTimeout(() => {
                    window.location.reload();
                }, 1500);
            } else {
                showNotification(data.message, 'error');
            }
        });
    };

    // Gestionar solicitudes de retiro (Aprobar/Rechazar)
    window.manageWithdrawal = function(solicitudId, action) {
        const formData = new FormData();
        formData.append('solicitud_id', solicitudId);
        formData.append('accion', action);

        fetch('/coordinator/approve_withdrawal', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                showNotification(data.message, 'success');
                setTimeout(() => {
                    window.location.reload();
                }, 1500);
            } else {
                showNotification(data.message, 'error');
            }
        });
    };

    // Crear sección con Builder
    const createSectionForm = document.getElementById('form-create-section');
    if (createSectionForm) {
        createSectionForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/coordinator/create_section', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification(data.message, 'success');
                    closeModal('modal-create-section');
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // Asignar Docente
    const assignTeacherForm = document.getElementById('form-assign-teacher');
    if (assignTeacherForm) {
        assignTeacherForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/coordinator/assign_teacher', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification(data.message, 'success');
                    closeModal('modal-assign-teacher');
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // Generar reporte de carrera
    const careerReportForm = document.getElementById('form-career-report');
    if (careerReportForm) {
        careerReportForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/coordinator/generate_career_report', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const consoleContent = document.getElementById('report-console-content');
                    if (consoleContent) {
                        consoleContent.textContent = data.report_content;
                        openModal('modal-view-report');
                        window.shouldReloadOnCloseReport = true;
                    }
                    showNotification(data.message, 'success');
                    closeModal('modal-career-report');
                } else {
                    showNotification(data.message, 'error');
                }
            });
        });
    }

    // =========================================================================
    // ACCIONES DE EDICIÓN DE AULA VIRTUAL (COORDINADOR)
    // =========================================================================
    window.openEditAulaModal = function(seccionId, currentLink) {
        const modal = document.getElementById('modal-edit-aula');
        const inputId = document.getElementById('edit-aula-seccion-id');
        const displayId = document.getElementById('edit-aula-seccion-display');
        const inputLink = document.getElementById('edit-aula-link');
        const selectPlat = document.getElementById('edit-aula-plataforma');

        if (modal && inputId && displayId && inputLink) {
            inputId.value = seccionId;
            displayId.textContent = seccionId;
            inputLink.value = currentLink;
            
            // Intentar adivinar la plataforma en base al enlace
            if (currentLink.toLowerCase().includes('zoom')) {
                selectPlat.value = 'ZOOM';
            } else {
                selectPlat.value = 'TEAMS';
            }
            
            openModal('modal-edit-aula');
        }
    };

    const editAulaForm = document.getElementById('form-edit-aula');
    if (editAulaForm) {
        editAulaForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            fetch('/coordinator/update_section_aula', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification(data.message, 'success');
                    closeModal('modal-edit-aula');
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            })
            .catch(err => {
                console.error("Error al actualizar aula virtual:", err);
                showNotification("Error de conexión.", "error");
            });
        });
    }

    // =========================================================================
    // IMPORTACIÓN DE ESTUDIANTES (COORDINADOR)
    // =========================================================================
    window.openImportStudentsModal = function(seccionId, capacidad) {
        const modal = document.getElementById('modal-import-students');
        const inputId = document.getElementById('import-students-seccion-id');
        const displayId = document.getElementById('import-students-seccion-display');
        const displayCap = document.getElementById('import-students-capacidad-display');
        const inputFile = document.getElementById('import-file');

        if (modal && inputId && displayId && displayCap) {
            inputId.value = seccionId;
            displayId.textContent = seccionId;
            displayCap.textContent = capacidad;
            if (inputFile) inputFile.value = ''; // Reset file input
            openModal('modal-import-students');
        }
    };

    const importStudentsForm = document.getElementById('form-import-students');
    if (importStudentsForm) {
        importStudentsForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);

            showNotification("Procesando archivo de Excel...", "success");

            fetch('/coordinator/import_students', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    showNotification(data.message, 'success');
                    closeModal('modal-import-students');
                    setTimeout(() => {
                        window.location.reload();
                    }, 1500);
                } else {
                    showNotification(data.message, 'error');
                }
            })
            .catch(err => {
                console.error("Error al importar estudiantes:", err);
                showNotification("Error de conexión al importar.", "error");
            });
        });
    }

    // =========================================================================
    // VISUALIZADOR DE CONSOLA DE REPORTES PREVIAMENTE GENERADOS
    // =========================================================================
    window.viewReportConsole = function(escapedContent) {
        const consoleContent = document.getElementById('report-console-content');
        if (consoleContent) {
            consoleContent.textContent = escapedContent;
            openModal('modal-view-report');
        }
    };


    // =========================================================================
    // SISTEMA DE NOTIFICACIONES TOAST FLOTANTES
    // =========================================================================
    function showNotification(message, type = 'success') {
        // Remover toasts previos si hay
        const oldToast = document.querySelector('.toast-notification');
        if (oldToast) oldToast.remove();

        const toast = document.createElement('div');
        toast.className = `toast-notification toast-${type}`;
        
        // Estilos rápidos en CSS inyectado para animación y posicionamiento
        toast.style.position = 'fixed';
        toast.style.bottom = '30px';
        toast.style.right = '30px';
        toast.style.padding = '14px 24px';
        toast.style.borderRadius = '8px';
        toast.style.fontSize = '0.9rem';
        toast.style.fontWeight = '500';
        toast.style.color = '#ffffff';
        toast.style.zIndex = '9999';
        toast.style.display = 'flex';
        toast.style.alignItems = 'center';
        toast.style.gap = '10px';
        toast.style.boxShadow = '0 10px 25px rgba(0,0,0,0.5)';
        toast.style.animation = 'slideIn 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        
        if (type === 'success') {
            toast.style.background = 'linear-gradient(135deg, #10b981 0%, #059669 100%)';
            toast.style.border = '1px solid rgba(16, 185, 129, 0.3)';
            toast.innerHTML = `<span>${message}</span>`;
        } else {
            toast.style.background = 'linear-gradient(135deg, #ef4444 0%, #dc2626 100%)';
            toast.style.border = '1px solid rgba(239, 68, 68, 0.3)';
            toast.innerHTML = `<span>${message}</span>`;
        }

        document.body.appendChild(toast);

        // Auto desvanecer en 4 segundos
        setTimeout(() => {
            toast.style.animation = 'slideOut 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
            setTimeout(() => {
                toast.remove();
            }, 300);
        }, 4000);
    }

    // Inyectar animaciones clave del Toast al DOM
    const styleSheet = document.createElement("style");
    styleSheet.textContent = `
        @keyframes slideIn {
            from { transform: translateY(100px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes slideOut {
            from { transform: translateY(0); opacity: 1; }
            to { transform: translateY(100px); opacity: 0; }
        }
    `;
    document.head.appendChild(styleSheet);

    // =========================================================================
    // NAVEGACIÓN DE MATERIAS (DOCENTE)
    // =========================================================================
    window.showSubjectStudents = function(sectionId) {
        const grid = document.getElementById('subjects-grid');
        const list = document.getElementById('students-view-container');
        
        if (grid && list) {
            grid.style.display = 'none';
            list.style.display = 'block';
            
            const tables = document.querySelectorAll('.section-students-table');
            tables.forEach(table => {
                if (table.getAttribute('data-section-id') === sectionId) {
                    table.style.display = 'block';
                } else {
                    table.style.display = 'none';
                }
            });
        }
    };

    window.hideSubjectStudents = function() {
        const grid = document.getElementById('subjects-grid');
        const list = document.getElementById('students-view-container');
        
        if (grid && list) {
            grid.style.display = 'grid';
            list.style.display = 'none';
            
            const searchInput = document.getElementById('student-search-input');
            if (searchInput) {
                searchInput.value = '';
            }
            
            const rows = document.querySelectorAll('.section-students-table tbody tr');
            rows.forEach(row => row.style.display = '');
        }
    };

    // =========================================================================
    // BUSCADOR UNIFICADO DE ESTUDIANTES (DOCENTE)
    // =========================================================================
    const searchInput = document.getElementById('student-search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();
            // Buscar la tabla de estudiantes que está visible
            const visibleTable = document.querySelector('.section-students-table[style*="display: block"]');
            if (visibleTable) {
                const rows = visibleTable.querySelectorAll('tbody tr');
                rows.forEach(row => {
                    if (row.cells.length > 1) {
                        const id = row.cells[0].textContent.toLowerCase();
                        const name = row.cells[1].textContent.toLowerCase();
                        const cedula = row.getAttribute('data-cedula') ? row.getAttribute('data-cedula').toLowerCase() : '';
                        
                        if (id.includes(query) || name.includes(query) || cedula.includes(query)) {
                            row.style.display = '';
                        } else {
                            row.style.display = 'none';
                        }
                    }
                });
            }
        });
    }

    // =========================================================================
    // CONSULTAR EXPEDIENTE/FICHA DETALLADA DE ESTUDIANTE (MODAL DOCENTE)
    // =========================================================================
    window.viewStudentDetails = function(studentId) {
        fetch(`/teacher/student_info/${studentId}`)
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success') {
                const est = data.data;
                
                // Generar tabla de calificaciones
                let gradesHtml = `
                    <table class="premium-table">
                        <thead>
                            <tr>
                                <th>Materia</th>
                                <th style="text-align: center;">Parcial 1</th>
                                <th style="text-align: center;">Parcial 2</th>
                                <th style="text-align: center;">Nota Final</th>
                                <th style="text-align: center;">Asistencia</th>
                                <th style="text-align: center;">Estado</th>
                            </tr>
                        </thead>
                        <tbody>
                `;
                
                est.notas.forEach(n => {
                    let badgeClass = 'badge-warning';
                    if (n.estado.includes('APROBADA')) badgeClass = 'badge-success';
                    else if (n.estado.includes('REPROBADA')) badgeClass = 'badge-danger';
                    
                    gradesHtml += `
                        <tr>
                            <td style="font-weight: 500;">${n.materia}</td>
                            <td style="text-align: center;">${n.parcial1.toFixed(2)}</td>
                            <td style="text-align: center;">${n.parcial2.toFixed(2)}</td>
                            <td style="text-align: center; font-weight: 700; color: var(--primary);">${n.nota_final.toFixed(2)}</td>
                            <td style="text-align: center;">${n.asistencia}%</td>
                            <td style="text-align: center;"><span class="badge ${badgeClass}">${n.estado}</span></td>
                        </tr>
                    `;
                });
                
                if (est.notas.length === 0) {
                    gradesHtml += `
                        <tr>
                            <td colspan="6" style="text-align: center; color: var(--text-secondary);">No registra asignaturas en este periodo.</td>
                        </tr>
                    `;
                }
                
                gradesHtml += `
                        </tbody>
                    </table>
                `;
                
                // Actualizar la vista del modal
                const contentDiv = document.getElementById('student-detail-content');
                if (contentDiv) {
                    contentDiv.innerHTML = `
                        <div style="display: flex; gap: 30px; flex-wrap: wrap;">
                            <div style="flex: 1; min-width: 280px; border-right: 1px solid var(--card-border); padding-right: 20px;">
                                <div style="text-align: center; margin-bottom: 20px;">
                                    <div style="width: 70px; height: 70px; border-radius: 50%; background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); margin: 0 auto 10px auto; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: 800; color: #ffffff; border: 2px solid rgba(0,0,0,0.05);">
                                        ${est.nombres[0]}${est.apellidos[0]}
                                    </div>
                                    <h4 style="font-size: 1.2rem; font-family: 'Merriweather', serif; color: var(--primary); margin-bottom: 2px;">${est.nombres} ${est.apellidos}</h4>
                                    <span style="font-size: 0.75rem; color: var(--text-secondary);">Código Estudiante: ${est.id_estudiante}</span>
                                </div>
                                <hr style="border: 0; border-top: 1px solid var(--card-border); margin: 15px 0;">
                                <div style="font-size: 0.85rem; display: flex; flex-direction: column; gap: 10px;">
                                    <div><span style="color: var(--text-secondary);">Cédula:</span> <strong style="float: right;">${est.cedula}</strong></div>
                                    <div><span style="color: var(--text-secondary);">Correo:</span> <strong style="float: right; font-size: 0.78rem;">${est.correo}</strong></div>
                                    <div><span style="color: var(--text-secondary);">Periodo Lectivo:</span> <strong style="float: right;">${est.nombre_periodo}</strong></div>
                                    <div><span style="color: var(--text-secondary);">Tipo Matrícula:</span> <strong style="float: right;">${est.tipo_matricula}</strong></div>
                                    <div><span style="color: var(--text-secondary);">Promedio General:</span> <strong style="float: right; color: var(--primary); font-weight: 700; font-size: 1rem;">${est.promedio.toFixed(2)}</strong></div>
                                </div>
                            </div>
                            <div style="flex: 2; min-width: 320px;">
                                <h4 style="font-size: 0.95rem; font-family: 'Merriweather', serif; color: var(--primary); margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.5px;">Calificaciones y Asistencia</h4>
                                <div class="table-container">
                                     ${gradesHtml}
                                </div>
                            </div>
                        </div>
                    `;
                }
                
                // Abrir la ventana modal
                openModal('modal-student-detail');
            } else {
                showNotification(data.message, 'error');
            }
        })
        .catch(err => {
            console.error('Error al obtener info del estudiante:', err);
            showNotification('Error al conectar con el servidor.', 'error');
        });
    };

    // =========================================================================
    // RENDERIZADO DEL HORARIO GRÁFICO (STUDENT)
    // =========================================================================
    const horariosDataEl = document.getElementById('horarios-data');
    const calendarGridBody = document.getElementById('calendar-grid-body');

    if (horariosDataEl && calendarGridBody) {
        let horariosList = [];
        try {
            horariosList = JSON.parse(horariosDataEl.textContent);
        } catch (e) {
            console.error("Error parsing horarios-data", e);
        }

        // Configuración de la cuadrícula
        // Días de la semana: de Lunes (Col 2) a Viernes (Col 6)
        const diasSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"];
        
        // Intervalos de 30 minutos desde las 07:00 hasta las 19:00 (24 filas de 30 min)
        // Fila 1: Cabecera (Lunes a Viernes) -> grid-row: 1
        // Fila 2: 07:00 - 07:30
        // Fila 3: 07:30 - 08:00
        // ...
        // Fila 25: 18:30 - 19:00

        const horaInicioBase = 7; // 07:00
        const totalFilas = 24;   // 12 horas * 2 bloques por hora = 24 bloques de 30 min

        // 1. Generar etiquetas de horas (columna 1) y celdas de fondo vacías
        for (let fila = 0; fila < totalFilas; fila++) {
            const indexFila = fila + 2; // +2 porque la fila 1 es la cabecera
            const totalMinutos = fila * 30;
            const hora = Math.floor(horaInicioBase + totalMinutos / 60);
            const minuto = totalMinutos % 60;
            const horaStr = `${hora.toString().padStart(2, '0')}:${minuto.toString().padStart(2, '0')}`;

            // Solo mostrar etiqueta de hora completa (ej: 07:00, 08:00...) en el lado izquierdo
            const isLabelRow = (minuto === 0);
            
            if (isLabelRow) {
                const timeLabelCell = document.createElement('div');
                timeLabelCell.className = 'calendar-time-label';
                timeLabelCell.style.gridRow = `${indexFila} / span 2`;
                timeLabelCell.textContent = horaStr;
                calendarGridBody.appendChild(timeLabelCell);
            }

            // Crear las celdas vacías del fondo para Lunes a Viernes
            for (let col = 0; col < 5; col++) {
                const bgCell = document.createElement('div');
                bgCell.className = `calendar-grid-cell col-${col + 2} row-${indexFila}`;
                bgCell.style.gridColumn = col + 2;
                bgCell.style.gridRow = indexFila;
                
                // Si es borde de hora completa (es decir, el final de la media hora :30, o sea fila impar en indexFila)
                if (indexFila % 2 === 1) {
                    bgCell.classList.add('hour-boundary');
                }
                calendarGridBody.appendChild(bgCell);
            }
        }

        // 2. Colocar las tarjetas de clases sobre la cuadrícula
        // Función para convertir "HH:MM" a índice de fila (0-indexed desde las 07:00)
        function timeToRowIndex(timeStr) {
            const [h, m] = timeStr.split(':').map(Number);
            const diffMinutos = (h - horaInicioBase) * 60 + m;
            return Math.round(diffMinutos / 30);
        }

        const diasColumnMap = {
            "Lunes": 2,
            "Martes": 3,
            "Miércoles": 4,
            "Jueves": 5,
            "Viernes": 6
        };

        // Renderizar cada horario de cada sección matriculada
        horariosList.forEach((hor) => {
            const startRowOffset = timeToRowIndex(hor.inicio);
            const endRowOffset = timeToRowIndex(hor.fin);
            
            const startRow = startRowOffset + 2;
            const spanRows = endRowOffset - startRowOffset;

            // Determinar los días en que se dicta la clase
            const diasClase = hor.dias || ["Lunes", "Miércoles", "Viernes"];

            diasClase.forEach(dia => {
                const col = diasColumnMap[dia];
                if (!col) return; // Si es sábado u otro no configurado en este grid

                // Crear tarjeta
                const card = document.createElement('div');
                const isVirtual = hor.modalidad.toLowerCase() === 'virtual';
                card.className = `calendar-class-card ${isVirtual ? 'mode-virtual' : 'mode-presencial'}`;
                card.style.gridColumn = col;
                card.style.gridRow = `${startRow} / span ${spanRows}`;
                
                card.innerHTML = `
                    <div class="class-materia" title="${hor.materia}">${hor.materia}</div>
                    <div class="class-details">
                        <span>Sección: <strong>${hor.seccion}</strong></span>
                        <span>Docente: <strong>${hor.docente.split(',')[0]}</strong></span>
                    </div>
                    <div class="class-footer">
                        <span>${hor.inicio} - ${hor.fin}</span>
                        <span>${isVirtual ? '💻' : '🏫'}</span>
                    </div>
                `;

                // Clic para abrir detalle
                card.addEventListener('click', () => {
                    showClassDetail(hor);
                });

                calendarGridBody.appendChild(card);
            });
        });

        // 3. Función para mostrar detalle de clase en modal
        function showClassDetail(hor) {
            const detailContent = document.getElementById('class-detail-content');
            if (!detailContent) return;

            const isVirtual = hor.modalidad.toLowerCase() === 'virtual';
            const badgeClass = isVirtual ? 'badge-warning' : 'badge-success';
            const badgeColor = isVirtual ? 'var(--accent)' : 'var(--primary)';
            const badgeBg = isVirtual ? 'rgba(15, 118, 110, 0.1)' : 'rgba(122, 27, 41, 0.05)';

            let virtualLinkHtml = '';
            if (isVirtual) {
                if (hor.aula) {
                    virtualLinkHtml = `
                        <div style="margin-top: 20px;">
                            <a href="${hor.aula}" target="_blank" class="btn btn-primary" style="display: flex; gap: 8px; width: 100%; text-decoration: none; align-items: center; justify-content: center; font-size: 0.9rem; background: var(--accent);">
                                💻 Unirse a Clase Virtual
                            </a>
                        </div>
                    `;
                } else {
                    virtualLinkHtml = `
                        <div style="margin-top: 15px; padding: 12px; background: var(--warning-bg); border-radius: var(--radius-sm); font-size: 0.85rem; border-left: 3px solid var(--warning); display: flex; align-items: center; gap: 8px;">
                            ⚠️ <span style="color: var(--warning);"><strong>Aula Virtual:</strong> Enlace no asignado aún por coordinación.</span>
                        </div>
                    `;
                }
            } else {
                virtualLinkHtml = `
                    <div style="margin-top: 15px; padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); font-size: 0.85rem; border-left: 3px solid var(--primary); display: flex; align-items: center; gap: 8px;">
                        🏫 <span><strong>Aula Asignada:</strong> Entorno Físico - Campus Universitario</span>
                    </div>
                `;
            }

            const diasFormat = (hor.dias || ["Lunes", "Miércoles", "Viernes"]).join(', ');

            detailContent.innerHTML = `
                <div style="display: flex; flex-direction: column; gap: 15px;">
                    <div>
                        <span class="badge ${badgeClass}" style="background: ${badgeBg}; border-color: ${badgeBg}; color: ${badgeColor}; font-size: 0.75rem; text-transform: uppercase; font-weight: 700; letter-spacing: 0.5px; padding: 4px 8px;">
                            ${hor.modalidad}
                        </span>
                        <h4 style="font-size: 1.25rem; font-family: 'Merriweather', serif; color: var(--primary); margin-top: 8px; line-height: 1.3;">${hor.materia}</h4>
                    </div>
                    
                    <hr style="border: 0; border-top: 1px solid var(--card-border);">
                    
                    <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.88rem;">
                        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-secondary);">Sección:</span><strong>${hor.seccion}</strong></div>
                        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-secondary);">Turno:</span><strong>${hor.turno}</strong></div>
                        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-secondary);">Días de Clase:</span><strong>${diasFormat}</strong></div>
                        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-secondary);">Horario de Entrada:</span><strong>${hor.inicio}</strong></div>
                        <div style="display: flex; justify-content: space-between;"><span style="color: var(--text-secondary);">Horario de Salida:</span><strong>${hor.fin}</strong></div>
                        <div style="display: flex; flex-direction: column; gap: 4px; margin-top: 4px;">
                            <span style="color: var(--text-secondary);">Docente Asignado:</span>
                            <strong style="color: var(--text-primary); font-size: 0.9rem; padding-left: 8px; border-left: 2px solid var(--card-border);">${hor.docente}</strong>
                        </div>
                    </div>

                    ${virtualLinkHtml}
                </div>
            `;

            openModal('modal-class-detail');
        }

        // 4. Toggle entre vistas (Calendario vs Lista)
        const btnViewGraphic = document.getElementById('btn-view-graphic');
        const btnViewList = document.getElementById('btn-view-list');
        const graphicContainer = document.getElementById('schedule-graphic-container');
        const listContainer = document.getElementById('schedule-list-container');

        if (btnViewGraphic && btnViewList && graphicContainer && listContainer) {
            btnViewGraphic.addEventListener('click', () => {
                btnViewGraphic.classList.add('active-view-btn');
                btnViewList.classList.remove('active-view-btn');
                graphicContainer.style.display = 'block';
                listContainer.style.display = 'none';
            });

            btnViewList.addEventListener('click', () => {
                btnViewList.classList.add('active-view-btn');
                btnViewGraphic.classList.remove('active-view-btn');
                graphicContainer.style.display = 'none';
                listContainer.style.display = 'block';
            });
        }
    }
});
