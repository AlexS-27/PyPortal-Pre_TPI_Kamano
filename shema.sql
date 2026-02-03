drop table if exists scores;
drop table if exists users;

create table users (
    id_user integer primary key autoincrement,
    username text not null unique,
    password text not null,
    created_at timestamp default current_timestamp
);

create table scores (
    id_score integer primary key autoincrement,
    value int not null,
    archived_at timestamp default current_timestamp,
    user_id integer not null,
    foreign key (user_id) references users (id_user)
        on delete cascade
);