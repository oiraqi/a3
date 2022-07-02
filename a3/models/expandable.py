from odoo import models


class Expandable(models.AbstractModel):
    _name = 'ix.expandable'
    _description = 'Expandable Mixin'

    def _resolve_action(self, action_id, domain, context=False):
        action = self.env['ir.actions.act_window']._for_xml_id(action_id)
        action['domain'] = domain
        if context:
            action['context'] = context		
        return action
    