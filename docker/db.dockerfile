FROM postgres:15.4-bookworm
RUN localedef -i ko_KR -c -f UTF-8 -A /usr/share/locale/locale.alias ko_KR.UTF-8 &&\
    ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime &&\
    echo "Asia/Seoul" > /etc/timezone

EXPOSE 5432
CMD ["postgres"]
