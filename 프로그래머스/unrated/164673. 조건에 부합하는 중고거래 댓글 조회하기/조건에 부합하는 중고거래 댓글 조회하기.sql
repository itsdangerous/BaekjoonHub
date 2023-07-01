SELECT board.title, board.board_id,
    reply.reply_id, reply.writer_id, reply.contents, date_format(reply.created_date, "%Y-%m-%d") as CREATED_DATE
from used_goods_board as board, used_goods_reply as reply
where year(board.created_date) = 2022 and month(board.created_date) = 10
    and board.board_id = reply.board_id
order by reply.created_date asc, board.title asc;