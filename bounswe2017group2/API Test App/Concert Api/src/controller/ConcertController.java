package controller;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.json.JSONException;

import dao.ConcertDao;
import model.Concert;

/**
 * Servlet implementation class ConcertController
 */
@WebServlet("/ConcertController")
public class ConcertController extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static int last_id=0;

    /**
     * Default constructor. 
     */
    public ConcertController() {
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		ConcertDao concertDao = new ConcertDao();
		 
			try {
				response.getWriter().append(concertDao.getAllConcerts().toString());
			} catch (JSONException e) {
				// TODO Auto-generated catch block
				response.getWriter().append("Something goes wrong!!");
			}
		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		
		Concert concert=new Concert();
		concert.setId(last_id++);
		concert.setArtist(request.getParameter("artist"));
		concert.setDate(request.getParameter("date"));
		concert.setLocation(request.getParameter("location"));
		
		ConcertDao concertDao=new ConcertDao();
		concertDao.createConcert(concert);
		
		response.getWriter().append("Concert created successfully");
		
		
	}

}
