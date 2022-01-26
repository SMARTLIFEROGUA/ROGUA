odoo.define('ks_dashboard_ninja.import_button', function(require) {

    "use strict";

    var core = require('web.core');
    var _t = core._t;
//    var Sidebar = require('web.Sidebar');
    var ListController = require('web.ListController');
    var framework = require('web.framework');
    var Dialog = require('web.Dialog');


    ListController.include({

        renderButtons: function($node) {
            this.ksIsAdmin = odoo.session_info.is_admin;
            this._super.apply(this, arguments);
            //On Click on our custom import button, call custom import function
            if (this.$buttons) {
                var import_button = this.$buttons.find('.ks_import_button');
                var import_input_button = this.$buttons.find('.ks_input_import_button');
                import_button.click(this.proxy('ks_import_button'));
                import_input_button.change(this.proxy('ksImportFileChange'));
            }
        },


       _getActionMenuItems: function (state) {
        if (!this.hasActionMenus || !this.selectedRecords.length) {
            return null;
        }
        const props = this._super(...arguments);
        const otherActionItems = [];
        if (this.modelName == "ks_dashboard_ninja.board"){
        if (this.isExportEnable) {
            otherActionItems.push({
                 description: _t("Export Dashboard"),
                callback: this.ks_dashboard_export.bind(this)
            });
        }
        if (this.archiveEnabled) {
            otherActionItems.push({
                description: _t("Archive"),
                callback: () => {
                    Dialog.confirm(this, _t("Are you sure that you want to archive all the selected records?"), {
                        confirm_callback: () => this._toggleArchiveState(true),
                    });
                }
            }, {
                description: _t("Unarchive"),
                callback: () => this._toggleArchiveState(false)
            });
        }
        if (this.activeActions.delete) {
            otherActionItems.push({
                description: _t("Delete"),
                callback: () => this._onDeleteSelectedRecords()
            });
        }}else{
            if (this.isExportEnable) {
            otherActionItems.push({
                description: _t("Export"),
                callback: () => this._onExportData()
            });
        }
        if (this.archiveEnabled) {
            otherActionItems.push({
                description: _t("Archive"),
                callback: () => {
                    Dialog.confirm(this, _t("Are you sure that you want to archive all the selected records?"), {
                        confirm_callback: () => this._toggleArchiveState(true),
                    });
                }
            }, {
                description: _t("Unarchive"),
                callback: () => this._toggleArchiveState(false)
            });
        }
        if (this.activeActions.delete) {
            otherActionItems.push({
                description: _t("Delete"),
                callback: () => this._onDeleteSelectedRecords()
            });
        }

        }
        return Object.assign(props, {
            items: Object.assign({}, this.toolbarActions, { other: otherActionItems }),
            context: state.getContext(),
            domain: state.getDomain(),
            isDomainSelected: this.isDomainSelected,
        });

    },

        ks_dashboard_export: function() {
            this.ks_on_dashboard_export(this.getSelectedIds());
        },

        ks_on_dashboard_export: function(ids) {
            var self = this;
            this._rpc({
                model: 'ks_dashboard_ninja.board',
                method: 'ks_dashboard_export',
                args: [JSON.stringify(ids)],
            }).then(function(result) {
                var name = "dashboard_ninja";
                var data = {
                    "header": name,
                    "dashboard_data": result,
                }
                framework.blockUI();
                self.getSession().get_file({
                    url: '/ks_dashboard_ninja/export/dashboard_json',
                    data: {
                        data: JSON.stringify(data)
                    },
                    complete: framework.unblockUI,
                    error: (error) => this.call('crash_manager', 'rpc_error', error),
                });
            })
        },

        ks_import_button: function(e) {
            var self = this;
            $('.ks_input_import_button').click();
        },

        ksImportFileChange: function(e) {
            var self = this;
            var fileReader = new FileReader();
            fileReader.onload = function() {
                $('.ks_input_import_button').val('');
                self._rpc({
                    model: 'ks_dashboard_ninja.board',
                    method: 'ks_import_dashboard',
                    args: [fileReader.result],
                }).then(function(result) {
                    if (result === "Success") {
                        framework.blockUI();
                        location.reload();
                    } else if (result.ks_skiped_items){
                        Dialog.alert(self, _t("Some Items can not be imported Need Dashboard Ninja pro "), {
                            confirm_callback: function() {
                                location.reload();
                            },
                            title: _t('All items can not be Imported'),
                        });

                    }
                });
            };
            fileReader.readAsText($('.ks_input_import_button').prop('files')[0]);
        },

        _updateButtons: function(mode) {
            if (this.$buttons) {
                if (mode === "edit") this.$buttons.find('.ks_import_button').hide();
                else if (mode === "readonly") this.$buttons.find('.ks_import_button').show();
                this._super.apply(this, arguments);
            }
        },
    });
    core.action_registry.add('ks_dashboard_ninja.import_button', ListController);
    return ListController;
});