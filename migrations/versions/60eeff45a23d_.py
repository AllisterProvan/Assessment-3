
from alembic import op
import sqlalchemy as sa



revision = '60eeff45a23d'
down_revision = '036bc17fc4a6'
branch_labels = None
depends_on = None


def upgrade():
    
    op.add_column('item', sa.Column('starting_bid', sa.Integer(), nullable=False))
    


def downgrade():
    
    op.drop_column('item', 'starting_bid')
    
