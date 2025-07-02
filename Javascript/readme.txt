1. Var, const, let
    var: chỉ nên sử dụng với trình duyệt cũ trước 2015
    const: Được thêm vào trình duyệt > 2015, khai báo hằng số, hằng số này không thể thay đổi giá trị
    let: Được thêm vào trình duyệt > 2015, khai báo biến, có thể thay đổi được
    ※ Có thể khai báo lại biến với var , nhưng const và let thì không
    ví dụ: 
        OK: Var x = 1;
            Var x;
        NG: Const x =1;
            Const x;
    ※ Const không thể khai báo hay gán giá trị lại nhưng có thể thay đổi property bên trong nếu là object

2. Object:
    Object.values(obj) ---> Trả ra list value của object, nếu object là array sẽ trả ra list thành phần của list
    Object.entries ---> Trả ra dữ liệu key và value tương ứng

3.Làm việc với array:
    3.1:Array.Map(): Duyệt qua từng phần tử của mảng và tạo ra 1 mảng mới
        Cú pháp: const newArray = array.map((element, index, array) => {
                                        // return giá trị mới cho phần tử
                                    });
        Giải thích:
            ☑️array : mảng chính
            ☑️callback(element,idex,array) : Hàm xử lí và trả ra phần tử cho mảng mới
                element: phần tử hiện tại
                idex: thứ tự của phần tử hiện tại trong mảng
                array: mảng gốc
            ☑️Ví dụ:
                const numbers = [1, 2, 3];
                const doubled = numbers.map(n => n * 2);
                console.log(doubled); // [2, 4, 6]

    3.2: Array.foreach(): Duyệt qua từng phần tử của mảng, thực hiện xử lí với phần tử đó, không tạo ra mảng mới và không return gì cả
        Cú pháp:    array.forEach((element, index, array) => {
                                // xử lý phần tử
                                });
        Giải thích:
            ☑️array : mảng cần check
            ☑️callback(element,idex,array) : hàm kiểm tra điều kiện, tham số truyền vào không nhất thiết phải đủ cả 3
                element: phần tử hiện tại
                idex: thứ tự của phần tử hiện tại trong mảng
                array: mảng gốc
            ☑️Ví dụ:    const fruits = ["apple", "banana", "cherry"];
                        fruits.forEach((fruit, index) => {
                            console.log(index + ":", fruit);
                        });

    3.2:Array.Some(): Nếu có ít nhất 1 phần tử trong mảng thoả mãn điều kiện thì output là true, ngược lại false
        Cú pháp: array.some(callback(element, index, array))
        Giải thích: 
            ☑️array : mảng cần check
            ☑️callback(element,idex,array) : hàm kiểm tra điều kiện, tham số truyền vào không nhất thiết phải đủ cả 3
                element: phần tử hiện tại
                idex: thứ tự của phần tử hiện tại trong mảng
                array: mảng gốc
            ☑️Ví dụ:
                const numbers = [1, 3, 5, 7, 8];
                const hasEven = numbers.some(n => n % 2 === 0);
                console.log(hasEven); // true (vì có số 8 là chẵn)

    3.3: Array.Every(): Nếu tất cả các phần tử trong mảng đều thoả mãn điều kiện thì output là true, ngược lại false
        Cú pháp: array.Every(callback(element, index, array))
        Giải thích: 
            ☑️array : mảng cần check
            ☑️callback(element,idex,array) : hàm kiểm tra điều kiện, tham số truyền vào không nhất thiết phải đủ cả 3
                element: phần tử hiện tại
                idex: thứ tự của phần tử hiện tại trong mảng
                array: mảng gốc
            ☑️Ví dụ:
                const numbers = [1, 3, 5, 7, 8];
                const hasEven = numbers.some(n => n % 2 === 0);
                console.log(hasEven); // False (vì chỉ có số 8 là chẵn)
