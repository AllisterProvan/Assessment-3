
from alembic import op
import sqlalchemy as sa



revision = '582482be0bd4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    
    op.add_column('item', sa.Column('item_image', sa.String(length=30), nullable=False))
   


def downgrade():
    
    op.drop_column('item', 'item_image')
    
