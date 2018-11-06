FROM php:7.0-alpine

RUN curl -sS https://getcomposer.org/installer | php -- --filename=composer --install-dir=/bin/ && composer self-update

WORKDIR /composer

RUN composer require phpunit/phpunit

CMD tail -f /dev/null