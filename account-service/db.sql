CREATE TABLE subscription_plan (
    id UUID PRIMARY KEY,
    plan_name VARCHAR NOT NULL,
    payment_methods VARCHAR, -- Array de métodos de pago
    price DECIMAL(10, 2)
);

CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    birth_date DATE NOT NULL,
    created_at TIMESTAMP,
    last_login TIMESTAMP,
    subscription_plan_id UUID,
    FOREIGN KEY (subscription_plan_id) REFERENCES subscription_plan (id)
);

CREATE TABLE auth (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    username VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    created_at TIMESTAMP NOT NULL,
    role VARCHAR NOT NULL,
    status VARCHAR NOT NULL,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

CREATE TABLE device (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    device_brand VARCHAR NOT NULL,
    device_model VARCHAR NOT NULL,
    ip_address VARCHAR, -- INET type
    last_used_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES "user" (id)
);

CREATE TABLE genre (
    id UUID PRIMARY KEY,
    genre_name VARCHAR NOT NULL
);

CREATE TABLE serie (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    thumbnail_url VARCHAR NOT NULL,
    trailer_url VARCHAR NOT NULL,
    release_date TIME NOT NULL
);

CREATE TABLE season (
    id UUID PRIMARY KEY,
    serie_id UUID NOT NULL,
    number_of_season INT NOT NULL,
    release_date TIME NOT NULL,
    FOREIGN KEY (serie_id) REFERENCES serie (id)
);

CREATE TABLE content (
    id UUID PRIMARY KEY,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    release_date DATE NOT NULL,
    duration VARCHAR NOT NULL,
    thumbnail_file VARCHAR NOT NULL,
    content_file VARCHAR NOT NULL,
    trailer_file VARCHAR,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP,
    episode_number INT,
    season_id UUID,
    FOREIGN KEY (season_id) REFERENCES season (id)
);

CREATE TABLE watch_history (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    content_id UUID NOT NULL,
    watched_at TIMESTAMP NOT NULL,
    last_position DOUBLE,
    FOREIGN KEY (user_id) REFERENCES "user" (id),
    FOREIGN KEY (content_id) REFERENCES content (id)
);

CREATE TABLE franchise (
    id UUID PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL
);

CREATE TABLE content_genre (
    content_id UUID NOT NULL,
    genre_id UUID NOT NULL,
    primary BOOLEAN,
    PRIMARY KEY (content_id, genre_id),
    FOREIGN KEY (content_id) REFERENCES content (id),
    FOREIGN KEY (genre_id) REFERENCES genre (id)
);

CREATE TABLE content_franchise (
    content_id UUID NOT NULL,
    franchise_id UUID NOT NULL,
    primary BOOLEAN,
    PRIMARY KEY (content_id, franchise_id),
    FOREIGN KEY (content_id) REFERENCES content (id),
    FOREIGN KEY (franchise_id) REFERENCES franchise (id)
);